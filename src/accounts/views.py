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
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Permission
# Create your views here.

User = get_user_model()

@login_required
@permission_required('accounts.add_professor', raise_exception=True)
def admin_professor(request):
    print("===========================")
    print(request.POST)
    print("===========================")

    modules = Module.objects.all()

    

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

@login_required
@permission_required('accounts.add_student', raise_exception=True)
@permission_required('accounts.delete_student', raise_exception=True)
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
            student_username = user.username
            subject = 'SQUARE Application - NO REPLY MESSAGE -'
            message = render_to_string('accounts/email_template.html', {'full_name':full_name, 'prof_username':student_username})
            student_mail = user.email


            send_mail(subject, message, '' ,[student_mail], fail_silently=False)


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
                permission = Permission.objects.get(codename='add_cour')
                user.user_permissions.add(permission)
                return redirect('upload')
            elif user.is_student == 1:
                print("User Is STUDENT")
                return redirect('documents')
        else:
            messages.error(request, "Invalid Input")
            return render(request, 'Square/index.html')
            
    
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
            messages.error(request, 'Username or Password invalid')

    return render(request, 'accounts/login.html')

@login_required
def admin_choice(request):
    
    return render(request, 'accounts/admin_choice.html')


        

        
def logout_user(request):
    logout(request)
    return redirect('login')



@login_required
@permission_required('content.add_cour', raise_exception=True)
def upload(request):
    current_user = request.user
    print(current_user.username)
    print(current_user.email)
    print(current_user.password)
    

    
    modules = Module.objects.filter(professor=current_user.id)
    


    cours = Cour.objects.filter(module_id__in=modules)
    tds = Td.objects.filter(module_id__in=modules)
    tps = Tp.objects.filter(module_id__in=modules)
    homeworks = homework.objects.filter(module_id__in=modules)
    corrections = correction.objects.filter(module_id__in=modules)

    if request.method=='POST' and 'cour_checked' in request.POST:
        cour_checked = request.POST.getlist("cour_checked")
        Cour.objects.filter(id__in=cour_checked).delete()
    
    if request.method=='POST' and 'td_checked' in request.POST:
        td_checked = request.POST.getlist("td_checked")
        Td.objects.filter(id__in=td_checked).delete()
    
    if request.method=='POST' and 'tp_checked' in request.POST:
        tp_checked = request.POST.getlist("tp_checked")
        Tp.objects.filter(id__in=tp_checked).delete()

    if request.method=='POST' and 'homework_checked' in request.POST:
        homework_checked = request.POST.getlist("homework_checked")
        homework.objects.filter(id__in=homework_checked).delete()

    if request.method=='POST' and 'correction_checked' in request.POST:
        correction_checked = request.POST.getlist("correction_checked")
        correction.objects.filter(id__in=correction_checked).delete()
        


    context = {
        'modules' : modules,
        'cours' : cours,
        'tds' : tds,
        'tps' : tps,
        'homeworks' : homeworks,
        'corrections' : corrections,
    }


    if request.method=='POST' and 'title' in request.POST :
        
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
            return redirect('upload')
        else:
            messages.error(request, 'Invalid Changes (Try again)')

    
    if request.method=='POST' and 'old_email' in request.POST and 'new_email' in request.POST:
        old_email = request.POST["old_email"]
        new_email = request.POST["new_email"]
        if old_email == current_user.email:
            User.objects.filter(id=current_user.id).update(email=new_email)
            return redirect('upload')
        else:
            messages.error(request, 'Invalid Changes (Try again)')

    if request.method=='POST' and 'new_password' in request.POST and 'confirm_password' in request.POST:
        new_password = request.POST["new_password"]
        confirm_password = request.POST["confirm_password"]

        print(current_user.password)
        print(confirm_password)

        if new_password == confirm_password:
            usr = User.objects.get(username=current_user.username)
            usr.set_password(new_password)
            usr.save()

            return redirect('logout')


        else:
            messages.error(request, 'Invalid Changes (Try again)')





    return render(request, "accounts/upload.html", context)


