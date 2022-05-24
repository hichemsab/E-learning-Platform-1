from email import message
from multiprocessing import context
from re import I
from django.shortcuts import redirect, render
from accounts.models import Speciality, Student
from content.models import *
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.contrib import messages



# Create your views here.

@login_required
def documents(request):

    speciality = Speciality.objects.get(student=request.user.id)  
    modules = Module.objects.filter(Speciality_id=speciality.id)
    modules_id = Module.objects.filter(Speciality_id=speciality.id).values_list('id', flat=True)
    
    cours = Cour.objects.filter(module_id__in=modules_id)
    tds = Td.objects.filter(module_id__in=modules_id)
    tps = Tp.objects.filter(module_id__in=modules_id)
    homeworks = homework.objects.filter(module_id__in=modules_id)
    corrections = correction.objects.filter(module_id__in=modules_id)
    announcements = announcement.objects.filter(speciality_id=speciality.id)


    context = {
        'modules' : modules,
        'cours' : cours,
        'tds' : tds,
        'tps' : tps,
        'homeworks' : homeworks,
        'corrections' : corrections,
        'announcements' : announcements,
    }

    return render(request, "content/documents.html", context)


def about(request):
    return render(request, "content/about.html")


def contact(request):
    if request.method == "POST":
        email_sender = request.POST['email_sender']
        name_sender = request.POST['name_sender']
        message = request.POST['message']

        # send an email
        if send_mail(
            ' Message From : ' + name_sender + '   Email : ' + email_sender,
            message,
            email_sender,
            ['esquare375@gmail.com'],
        ) : 
            return redirect('email_sent_succefully')

        else:
            message.error("Message not sent")

    return render(request, "content/contact.html")

def email_sent_succefully(request):

    return render(request, "content/email_sent_succefully.html")