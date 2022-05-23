from django.urls import path
from accounts.views import  login_user, logout_user, upload, login_administrator, admin_choice, admin_professor, admin_student
from django.conf import settings
from django.conf.urls.static import static


#urls

urlpatterns = [
    path('login/', login_user, name="login"),
    path('logout/', logout_user, name="logout"),
    path('upload/', upload, name="upload"),
    path('login_administrator/', login_administrator, name="login_administrator"),
    path('admin_choice/', admin_choice, name="admin_choice"),
    path('admin_professor/', admin_professor, name="admin_professor"),
    path('admin_student/', admin_student, name="admin_student"),
]


