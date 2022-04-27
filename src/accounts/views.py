from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate, get_user_model
from accounts.models import Professor, User 
from content.models import Module
# Create your views here.

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
        return redirect('upload')

    return render(request, 'accounts/signup.html')
def login_user(request):
    if request.user.is_authenticated:
        logout(request)
    if request.method == "POST" :
        # Connecter l'utilisateur
        print("POst !!")
        username = request.POST.get("username")
        print(username)
        password = request.POST.get("password")
        print(password)
        
        user = authenticate(username=username, password=password)
        print(user)
        if user:
            print("User is not none")
            login(request, user)
            if User.is_professor:
                return redirect('upload')
        else:
            print("user is none")
    
    print("hhhhhhh")
    return render(request, 'accounts/login.html')

def logout_user(request):
    logout(request)
    return redirect('index')

def upload(request):
    current_user = request.user
    print(current_user.id)
    mod1, mod2, mod3 = Module.objects.filter(professor=current_user.id)

    context = {
    'mod1': mod1,
    'mod2': mod2,
    'mod3': mod3,
  }
    return render(request, "accounts/upload.html", context)
