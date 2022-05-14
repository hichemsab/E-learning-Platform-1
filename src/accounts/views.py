import email
from email import message
import imp
from secrets import choice
from turtle import title
from unicodedata import name
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate, get_user_model
from accounts.models import Professor, Speciality, Student, User 
from content.models import Module
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.core.files.storage import FileSystemStorage
from content.models import Module, Cour, Td, Tp, homework, correction
from django.core.mail import  send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.db.models import F
from content.views import documents

# Create your views here.

User = get_user_model()
def admin_professor(request):
    print("===========================")
    print(request.POST)
    print("===========================")

    modules = Module.objects.all()[29:33]

    

    context = {
    'modules': modules,
  }



    if request.method == "POST" and "gender" in request.POST :
        print(" first condition")
        # Traiter le formulaire
        last_name = request.POST.get("lastname")
        first_name = request.POST.get("firstname")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")
        gender = request.POST.get("gender")
        user = User.objects.create_user(last_name=last_name,
                                        first_name=first_name,
                                        email=email,
                                        username=username, 
                                        password=password,
                                        is_professor=True,
                                        gender=gender)

        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        modules = request.POST.getlist("modules")
        print(modules)
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

        if user:

            prof = Professor.objects.create(user_id=user.id) 

            for module in modules:
                prof.modules.add(module)
            
            

            messages.success(request, "Professor added succesfully .")


            full_name = user.first_name + " " + user.last_name
            prof_username = user.username
            subject = 'SQUARE Application - NO REPLY MESSAGE -'
            message = render_to_string('accounts/email_template.html', {'full_name':full_name, 'prof_username':prof_username})
            prof_mail = user.email


            send_mail(subject, message, '' ,[prof_mail], fail_silently=False)

            print("FINISHH")
    
    
    elif request.method == "POST"  :
        username = request.POST.get("username")
        prof = User.objects.filter(username=username, is_professor=True)
        sure = request.POST.get("Check")
        print(sure)

        if sure and prof:
            prof.delete()
            messages.success(request, "Professor deleted succesfully .")
        elif not sure:
            messages.error(request, "You have to be sure")
        elif not prof:
            messages.error(request, "Prof doesnt exist")

        
    
    return render(request, "accounts/admin_professor.html", context)

def admin_student(request):
    print("===========================")
    print(request.POST)
    print("===========================")

    specialities = Speciality.objects.all()

    print(specialities)



    context = {
        'specialities' : specialities,
  }


    if request.method == "POST" and "gender" in request.POST :
        print(" first condition")
        # Traiter le formulaire
        last_name = request.POST.get("lastname")
        first_name = request.POST.get("firstname")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")
        gender = request.POST.get("gender")
        user = User.objects.create_user(last_name=last_name,
                                        first_name=first_name,
                                        email=email,
                                        username=username, 
                                        password=password,
                                        is_student=True,
                                        gender=gender)
        if user:

            chosen_speciality = request.POST.get("Speciality")

            print("chosen_speciality :" )
            print(chosen_speciality)
    
            
            student = Student.objects.create(user_id=user.id, speciality_id=chosen_speciality)
            
                

            


            



            messages.success(request, "Student added succesfully .")

            full_name = user.first_name + " " + user.last_name
            prof_username = user.username
            subject = 'SQUARE Application - NO REPLY MESSAGE -'
            message = render_to_string('accounts/email_template.html', {'full_name':full_name, 'prof_username':prof_username})
            prof_mail = user.email


            send_mail(subject, message, '' ,[prof_mail], fail_silently=False)


    elif request.method == "POST"  :
        username = request.POST.get("username")
        student = User.objects.filter(username=username, is_student=True)
        sure = request.POST.get("Check")
        print(sure)

        if sure and student :
            student.delete()
            messages.success(request, "Student deleted succesfully .")
        elif not sure:
            messages.error(request, "You have to be sure")
        elif not student:
            messages.error(request, "Student doesnt exist")
    return render(request, "accounts/admin_student.html", context)
    


def login_user(request):
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
            if user.is_professor == 1:
                print("User Is PROFESSOR")
                return redirect('upload')
            elif user.is_student == 1:
                print("User Is STUDENT")
                return redirect('documents')
        else:
            print("user is none")
    
    else:

        return render(request, 'Square/index.html')

def login_administrator(request):
    if request.method == "POST" :
        username = request.POST.get("username")
        print(username)
        password = request.POST.get("password")
        print(password)
        
        user = authenticate(username=username, password=password)
        if user :
            if user.is_staff == 1:
                login(request, user)
                return redirect('admin_choice')
            else:
                messages.error(request, 'you are not part of the administration')
        
        else:
            messages.error(request, 'username or password not valid')

    return render(request, 'accounts/login.html')

def admin_choice(request):
    
    return render(request, 'accounts/admin_choice.html')


        

        
def logout_user(request):
    logout(request)
    return redirect('login')




def upload(request):
    current_user = request.user
    print(current_user.username)
    print(current_user.email)
    print(current_user.password)
    print(request.POST)

    if len(Module.objects.filter(professor=current_user.id))==2:
        mod1, mod2 = Module.objects.filter(professor=current_user.id)

        context = {
    'mod1': mod1,
    'mod2': mod2,
  }

    elif len(Module.objects.filter(professor=current_user.id))==3:
        mod1, mod2, mod3 = Module.objects.filter(professor=current_user.id)

        context = {
    'mod1': mod1,
    'mod2': mod2,
    'mod3': mod3,
  }
    elif len(Module.objects.filter(professor=current_user.id))==4:
        mod1, mod2, mod3, mod4 = Module.objects.filter(professor=current_user.id)
        context = {
    'mod1': mod1,
    'mod2': mod2,
    'mod3': mod3,
    'mod4': mod4,
  }


    if request.method=='POST' :
        
        chosen_module = request.POST["modu"]
        title = request.POST["title"]
        chosen_option = request.POST["Option"]
        uploaded_file = request.FILES['fichier']
        print("*****************************************")
        print(chosen_module)
        print("*****************************************")
        print(title)
        print("*****************************************")
        print(chosen_option)
        print("*****************************************")
        print(uploaded_file)
        print("*****************************************")
        
        identifiant = Module.objects.get(name=chosen_module).id
        print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
        print(identifiant)
        print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMM")

        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)

        if chosen_option == "Courses":

            cr = Cour.objects.create(title=title, cour = uploaded_file, module_id = identifiant)

        elif chosen_option == "Home-workes":
            hw = homework.objects.create(title=title, quizz = uploaded_file, module_id = identifiant)
        
        elif chosen_option == "TD":
            td = Td.objects.create(title=title,td = uploaded_file, module_id = identifiant)

        elif chosen_option == "TP":
            tp = Tp.objects.create(title=title, tp = uploaded_file, module_id = identifiant)

        elif chosen_option == "Correction":
            c = correction.objects.create(title=title, correction = uploaded_file, module_id = identifiant)
        
        
        
    
    if request.method=='POST' and 'old_username' in request.POST and 'new_username' in request.POST:
        old_username = request.POST["old_username"]
        new_username = request.POST["new_username"]
        if old_username == current_user.username :
            User.objects.filter(id=current_user.id).update(username=new_username)
        else:
            messages.error(request, 'User name  not changed (check settings)')

    
    if request.method=='POST' and 'old_email' in request.POST and 'new_email' in request.POST:
        old_email = request.POST["old_email"]
        new_email = request.POST["new_email"]
        if old_email == current_user.email:
            User.objects.filter(id=current_user.id).update(email=new_email)
        else:
            messages.error(request, 'email not changed (check settings)')

    if request.method=='POST' and 'old_password' in request.POST and 'new_password' in request.POST:
        old_password = request.POST["old_password"]
        new_password = request.POST["new_password"]

        print(current_user.password)
        print(old_password)

        if check_password(old_password, current_user.password):
            usr = User.objects.get(username=current_user.username)
            usr.set_password(new_password)
            usr.save()
        else:
            messages.error(request, 'Password not changed (check settings)')




    return render(request, "accounts/upload.html", context)


