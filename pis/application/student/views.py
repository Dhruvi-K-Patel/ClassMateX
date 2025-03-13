from django.shortcuts import render,redirect
from django.http import HttpResponse
from faculty.models import faculty
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.contrib.auth.models import User
from .forms import UserForm,UserProfileForm,AssignmentForm
from django.template import RequestContext
from django.conf import settings
from departments.models import departments
from timetable.models import TimeTable
from lab.models import Lab
from attendance.models import Attendance
from ebook.models import Ebook
from assignment.models import Assignment
from noticebord.models import NoticeBoard
from events.models import Studentevntes
# Create your views here.

def index(request):
    return render(request,"index.html")


def StudentLogin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('StundetDashboard')
        else:
            return render(request,"students/login.html",{'msg':"Invalid Username Or Password"})
    return render(request,"students/login.html")

@login_required(login_url='StudentLogin')
def Dashboard(request):
    return render(request,"students/index.html")


def StudentRegister(request):
    context = RequestContext(request)
    registered = False
    if request.method == "POST":
        uform = UserForm(data = request.POST)
        pform = UserProfileForm(request.POST,request.FILES)
        if uform.is_valid() and pform.is_valid():
            user = uform.save()
            pw = user.password
            user.set_password(pw)
            user.save()
            profile = pform.save(commit = False)
            profile.user = user
            profile.save()
            #save_file(request.FILES['Profile_pic'])
            registered = True
            return redirect('StudentLogin')
        else:
            print("errors")
    else:
        uform = UserForm()
        pform = UserProfileForm()
    return render(request,"students/register.html", {'uform': uform, 'pform': pform, 'registered': registered }, context)

# def save_file(file, path=''):
#         filename = file._get_name()
#         fd = open('%s/%s' % (MEDIA_ROOT, str(path) + str(filename)), 'wb' )
#         for chunk in file.chunks():
#                 fd.write(chunk)
#         fd.close()
# # class StudentSignUpView(CreateView):
# #     pass

@login_required(login_url='StudentLogin')
def FacultiesList(request):
    facultylist = faculty.objects.all()
    context = {
        'facultylist':facultylist
    }
    return render(request,"students/all-professors.html",context)



@login_required(login_url='StudentLogin')
def departmentsview(request):
    departmentsviewf = departments.objects.all()
    return render(request,"students/departmentsView.html",{'departmentsviewf':departmentsviewf})



@login_required(login_url='StudentLogin')
def NoticeBoardStudent(request):
    NoticeBoardStude = NoticeBoard.objects.all()
    return render(request,"students/index.html",{'NoticeBoardStude':NoticeBoardStude})






@login_required(login_url='StudentLogin')
def studenteventsf(request):
    Studentevntesview = Studentevntes.objects.all()
    return render(request,"students/eventsView.html",{'Studentevntesview':Studentevntesview})








@login_required(login_url='StudentLogin')
def LabView(request):
    LabViewstudent = Lab.objects.all()
    return render(request,"students/LabView.html",{'LabViewstudent':LabViewstudent})



@login_required(login_url='StudentLogin')
def EbookView(request):
    EbookViewstudent = Ebook.objects.all()
    return render(request,"students/EbookView.html",{'EbookViewstudent':EbookViewstudent})




@login_required(login_url='StudentLogin')
def timetable(request):
    forms = TimeTable.objects.all()
    return render(request,"students/studenttimeble.html",{'forms':forms})



@login_required(login_url='StudentLogin')
def viewattendence(request):
    User = request.user
    sattendance = Attendance.objects.all()
    return render(request,"students/studentAttendance.html",{'sattendance':sattendance})    


@login_required(login_url='StudentLogin')
def StudentAssignment(request):
    AddAssignmentAdds = AssignmentForm(request.POST,request.FILES)
    if request.method == "POST":
        if AddAssignmentAdds.is_valid():
            AddAssignmentAdds.save()
            return redirect('sdAssignmentview')
        else:
            print("error")
    return render(request,"students/StudentAssignment.html",{'AddAssignmentAdds':AddAssignmentAdds})



@login_required(login_url='StudentLogin')
def sdAssignmentview(request):
    Assignmentlist = Assignment.objects.all()
    return render(request,"students/ViewstudentAssignment.html",{'Assignmentlist':Assignmentlist})


def logout_views(request):
    logout(request)
    return redirect('StudentLogin')