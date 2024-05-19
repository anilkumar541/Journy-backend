from django.urls import path
from .views import UserRegistrationView, LoginView, UserProfileView, ChangePasswordView, SendForgotPasswordEmailView, ForgotPasswordUpdateView

urlpatterns = [
    path("register/", UserRegistrationView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("user_profile/", UserProfileView.as_view(), name="user_profile"),
    path("change_password/", ChangePasswordView.as_view(), name="change_password"),
    path("send_forgot_password_email/", SendForgotPasswordEmailView.as_view(), name="send_forgot_password_email"),
    path("reset_forgot_password/<encoded_user_id>/<token>/", ForgotPasswordUpdateView.as_view(), name="reset_forgot_password"),
]

# MQ/c2l4sq-2af3da87984df1b601e30405d82d2e95