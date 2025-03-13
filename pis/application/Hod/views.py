from django.shortcuts import render
from faculty.models import *

# Create your views here.

def HodLogin(request):
    return render(request,"hod/login.html")

def Dashboard(request):
    return render(request,"hod/index.html")

def HodRegister(request):
    return render(request,"hod/register.html")


def FacultiesListHod(request):
    facultylist = faculty.objects.all()
    context = {
        'facultylist':facultylist
    }
    return render(request,"hod/all-professors-hod.html",context)