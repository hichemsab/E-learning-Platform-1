import email
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model, login, logout, authenticate
from django.contrib.auth.decorators import login_required


def upload(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, "professors/upload.html")


User = get_user_model()
def signup(request):
    if request.method == "POST":
        # Traiter le formulaire
        last_name = request.POST.get("lastname")
        first_name = request.POST.get("firstname")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = User.objects.create_user(last_name=last_name,
                                        first_name=first_name,
                                        email=email,
                                        username=username, 
                                        password=password)
        login(request, user)
        return redirect('professors-upload')

    return render(request, 'professors/signup.html')


def login_user(request):
    if request.method == "POST":
        # Connecter l'utilisateur
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('professors-upload')
    
    return render(request, 'professors/login.html')

def logout_user(request):
    logout(request)
    return redirect('index')
