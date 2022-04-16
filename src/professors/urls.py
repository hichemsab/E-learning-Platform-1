from django.urls import path
from professors.views import upload, signup, logout_user, login_user




urlpatterns = [
    path('signup/', signup, name="professors-signup"),
    path('upload/', upload, name="professors-upload"),
    path('login/', login_user, name="login"),
    path('logout/', logout_user, name="logout"),
]