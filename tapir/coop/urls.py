from django.urls import path

from tapir.coop import views

app_name = "coop"
urlpatterns = [
    path(
        "share/create/user/<int:user_pk>/",
        views.ShareOwnershipCreateForUserView.as_view(),
        name="share_create_for_user",
    ),
    path(
        "share/update/<int:pk>/",
        views.ShareOwnershipUpdateView.as_view(),
        name="share_update",
    ),
    path("user/draft/", views.DraftUserListView.as_view(), name="draftuser_list"),
    path(
        "user/draft/create",
        views.DraftUserCreateView.as_view(),
        name="draftuser_create",
    ),
    path(
        "user/draft/<int:pk>/edit",
        views.DraftUserUpdateView.as_view(),
        name="draftuser_update",
    ),
    path(
        "user/draft/<int:pk>",
        views.DraftUserDetailView.as_view(),
        name="draftuser_detail",
    ),
    path(
        "user/draft/<int:pk>/delete",
        views.DraftUserDeleteView.as_view(),
        name="draftuser_delete",
    ),
    path(
        "user/draft/<int:pk>/signed_membership_agreement",
        views.mark_signed_membership_agreement,
        name="mark_draftuser_signed_membership_agreement",
    ),
    path(
        "user/draft/<int:pk>/attended_welcome_session",
        views.mark_attended_welcome_session,
        name="mark_draftuser_attended_welcome_session",
    ),
    path(
        "user/draft/<int:pk>/membership_agreement",
        views.DraftUserMembershipAgreementView.as_view(),
        name="draftuser_membership_agreement",
    ),
    path(
        "user/draft/<int:pk>/create_user",
        views.create_user_from_draftuser,
        name="draftuser_create_user",
    ),
    path(
        "member/",
        views.ActiveShareOwnerListView.as_view(),
        name="active_shareowner_list",
    ),
    path(
        "member/<int:pk>/membership_confirmation",
        views.ShareOwnerMembershipConfirmationView.as_view(),
        name="shareowner_membership_confirmation",
    ),
    path(
        "user/draft/<int:pk>/register_payment_cash",
        views.register_draftuser_payment_cash,
        name="register_draftuser_payment_cash",
    ),
    path(
        "user/draft/<int:pk>/register_payment_bank",
        views.register_draftuser_payment_bank,
        name="register_draftuser_payment_bank",
    ),
]