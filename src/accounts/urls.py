from django import views
from django.urls import path
from accounts.views import  login_user, logout_user, upload, login_administrator, admin_choice, admin_professor, admin_student
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

#urls

urlpatterns = [
    path('login/', login_user, name="login"),
    path('logout/', logout_user, name="logout"),
    path('upload/', upload, name="upload"),
    path('login_administrator/', login_administrator, name="login_administrator"),
    path('admin_choice/', admin_choice, name="admin_choice"),
    path('admin_professor/', admin_professor, name="admin_professor"),
    path('admin_student/', admin_student, name="admin_student"),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_form.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_done.html"), name="password_reset_complete"),
]


