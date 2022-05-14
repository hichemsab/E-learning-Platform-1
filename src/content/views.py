from multiprocessing import context
from re import I
from django.shortcuts import render
from accounts.models import Speciality, Student
from content.models import *

# Create your views here.


def documents(request):

    speciality = Speciality.objects.get(student=request.user.id)  
    modules = Module.objects.filter(Speciality_id=speciality.id)
    modules_id = Module.objects.filter(Speciality_id=speciality.id).values_list('id', flat=True)
    
    cours = Cour.objects.filter(module_id__in=modules_id)
    tds = Td.objects.filter(module_id__in=modules_id)
    tps = Tp.objects.filter(module_id__in=modules_id)
    homeworks = homework.objects.filter(module_id__in=modules_id)
    corrections = correction.objects.filter(module_id__in=modules_id)

        
    context = {
        'modules' : modules,
        'cours' : cours,
        'tds' : tds,
        'tps' : tps,
        'homeworks' : homeworks,
        'corrections' : corrections,
    }

    return render(request, "content/documents.html", context)
