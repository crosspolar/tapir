import datetime

from django.db import transaction

from tapir.accounts.models import TapirUser
from tapir.coop.models import MembershipResignation, ShareOwnership, MembershipPause
from tapir.shifts.models import (
    ShiftAttendanceTemplate,
    ShiftAttendance,
)
from tapir.utils.shortcuts import get_timezone_aware_datetime


class MembershipResignationService:
    @staticmethod
    @transaction.atomic
    def update_shifts_and_shares(resignation: MembershipResignation):
        tapir_user: TapirUser = getattr(resignation.share_owner, "user", None)

        shares = ShareOwnership.objects.filter(share_owner=resignation.share_owner)

        match resignation.resignation_type:
            case MembershipResignation.ResignationType.BUY_BACK:
                new_end_date = resignation.cancellation_date.replace(day=31, month=12)
                new_end_date = new_end_date.replace(year=new_end_date.year + 3)
                resignation.pay_out_day = new_end_date
                resignation.save()
                shares.update(end_date=new_end_date)
                return
            case MembershipResignation.ResignationType.GIFT_TO_COOP:
                shares.update(end_date=resignation.cancellation_date)
            case MembershipResignation.ResignationType.TRANSFER:
                shares_to_create = [
                    ShareOwnership(
                        share_owner=resignation.transferring_shares_to,
                        start_date=resignation.cancellation_date,
                    )
                    for _ in shares
                ]
                ShareOwnership.objects.bulk_create(shares_to_create)
                shares.update(end_date=resignation.cancellation_date)
            case _:
                raise ValueError(
                    f"Unknown resignation type: {resignation.resignation_type}"
                )

        if not tapir_user:
            return

        MembershipResignationService.update_shifts(
            tapir_user=tapir_user, resignation=resignation
        )

    @staticmethod
    def update_shifts(tapir_user: TapirUser, resignation: MembershipResignation):
        start_date = get_timezone_aware_datetime(
            resignation.cancellation_date, datetime.time()
        )

        for attendance_template in ShiftAttendanceTemplate.objects.filter(
            user=tapir_user
        ):
            attendance_template.cancel_attendances(start_date)
            attendance_template.delete()

        attendances = ShiftAttendance.objects.filter(
            user=tapir_user,
            slot__shift__start_time__gte=start_date,
            state__in=ShiftAttendance.STATES_WHERE_THE_MEMBER_IS_EXPECTED_TO_SHOW_UP,
        )
        attendances.update(state=ShiftAttendance.State.CANCELLED)

    @staticmethod
    @transaction.atomic
    def delete_end_dates(member: MembershipResignation):
        ShareOwnership.objects.filter(share_owner=member.share_owner).update(
            end_date=None
        )

    @staticmethod
    def delete_shareowner_membershippauses(resignation: MembershipResignation):
        for pause in MembershipPause.objects.filter(
            share_owner=resignation.share_owner
        ):
            if pause.end_date is not None:
                if resignation.pay_out_day is not None:
                    if resignation.pay_out_day <= pause.end_date:
                        pause.update(end_date=resignation.pay_out_day)
                    elif pause.start_date > resignation.pay_out_day:
                        pause.delete()
                else:
                    if resignation.cancellation_date <= pause.end_date:
                        pause.update(end_date=resignation.cancellation_date)
                    elif pause.start_date > resignation.cancellation_date:
                        pause.delete()
            else:
                pause.update(end_date=resignation.cancellation_date)
