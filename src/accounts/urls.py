from django.urls import path
from accounts.views import login_user, logout_user, upload, signup


#urls

urlpatterns = [
    path('login/', login_user, name="login"),
    path('logout/', logout_user, name="logout"),
    path('upload/', upload, name="upload"),
    path('signup/', signup, name="signup"),
]