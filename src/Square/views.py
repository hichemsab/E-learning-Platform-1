


from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "Square/index.html")

def choice(request):
    return render(request, "Square/choice.html")

    