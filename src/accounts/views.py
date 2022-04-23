from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate


# Create your views here.

def login_user(request):
    if request.method == "POST":
        # Connecter l'utilisateur
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return render(request, "accounts/connected.html")
    
    return render(request, 'accounts/login.html')

def logout_user(request):
    logout(request)
    return redirect('index')


        
