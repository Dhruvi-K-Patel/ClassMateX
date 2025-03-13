from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .forms import UserForm,UserProfileForm,TimeTableForm,EbookAdd,AttendanceForm,AddAssignment
from django.template import RequestContext
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from student.models import Student
from timetable.models import TimeTable
from assignment.models import Assignment
from lab.models import Lab
from departments.models import departments
from attendance.models import Attendance
from ebook.models import Ebook
from events.models import Studentevntes

# Create your views here.

def Facultieslogin(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('facultiDashboard')
		else:
			return render(request,"Faculties/login.html",{'msg':"Invalid Username Or Password"})
	return render(request,"Faculties/login.html")

@login_required(login_url='Facultieslogin')
def facultiDashboard(request):
    return render(request,"Faculties/index.html")


@login_required(login_url='Facultieslogin')
def Assignmentview(request):
	Assignmentlist = Assignment.objects.all()
	return render(request,"Faculties/Assignment.html",{'Assignmentlist':Assignmentlist})





@login_required(login_url='Facultieslogin')
def Assignmentviewadd(request):
	AddAssignmentAdds = AddAssignment(request.POST,request.FILES)
	if request.method == "POST":
		if AddAssignmentAdds.is_valid():
			AddAssignmentAdds.save()
			return redirect('Assignmentview')
		else:
			print("error")
	return render(request,"Faculties/AddAssignment.html",{'AddAssignmentAdds':AddAssignmentAdds})





@login_required(login_url='Facultieslogin')
def studentevents(request):
    Studentevntesviewf = Studentevntes.objects.all()
    return render(request,"Faculties/eventsView.html",{'Studentevntesviewf':Studentevntesviewf})








@login_required(login_url='Facultieslogin')
def AdAssignmentview(request):
	Assignmentlist = Assignment.objects.all()
	return render(request,"Faculties/Assignment.html",{'Assignmentlist':Assignmentlist})




@login_required(login_url='Facultieslogin')
def labView(request):
	Lablist = Lab.objects.filter(status=True)
	return render(request,"Faculties/labView.html",{'Lablist':Lablist})


@login_required(login_url='Facultieslogin')
def AddStudentAttendance(request):
	AttendanceFormf = AttendanceForm(request.POST)
	if request.method == "POST":
		if AttendanceFormf.is_valid():
			AttendanceFormf.save()
			return redirect('AddStudentAttendance')
		else:
			print("error")
	return render(request,"Faculties/AddStudentAttendance.html",{'AttendanceFormf':AttendanceFormf})




@login_required(login_url='Facultieslogin')
def viewattendencef(request):
    sattendancef = Attendance.objects.all()
    return render(request,"Faculties/studentAttendance.html",{'sattendancef':sattendancef})    



@login_required(login_url='Facultieslogin')
def EbookViewf(request):
    EbookViewFaculties = Ebook.objects.all()
    return render(request,"Faculties/EbookView.html",{'EbookViewFaculties':EbookViewFaculties})


@login_required(login_url='Facultieslogin')
def addEbookViewf(request):
    EbookaddFaculties = EbookAdd(request.POST,request.FILES)
    if request.method == "POST":
    	if EbookaddFaculties.is_valid():
    		EbookaddFaculties.save()
    		return redirect('EbookViewf')
    	else:
    		print("Errors")

    return render(request,"Faculties/EbookAdd.html",{'EbookaddFaculties':EbookaddFaculties})





@login_required(login_url='Facultieslogin')
def departmentsview(request):
	departmentsviewf = departments.objects.all()
	return render(request,"Faculties/departmentsView.html",{'departmentsviewf':departmentsviewf})

@login_required(login_url='Facultieslogin')
def timetable(request):
	forms = TimeTable.objects.all()
	return render(request,"Faculties/studenttimeble.html",{'forms':forms})

def FacultiesRegister(request):
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
			return redirect('Facultieslogin')
		else:
			print("errors")
	else:
		uform = UserForm()
		pform = UserProfileForm()
	return render(request,"Faculties/register.html",{'uform': uform, 'pform': pform, 'registered': registered }, context)


@login_required(login_url='Facultieslogin')
def allstudents(request):
	student = Student.objects.all()
	return render(request,"Faculties/allstudents.html",{'student':student})


@login_required(login_url='Facultieslogin')
def studentProfile(request,id):
	student = Student.objects.filter(id=id)
	return render(request,"Faculties/student-profile.html",{'student':student})


@login_required(login_url='Facultieslogin')
def addstudent(request):
	return render(request,"Faculties/addstudent.html")



def logout_view(request):
    logout(request)
    return redirect('Facultieslogin')

# def save_file(file, path=''):
#         filename = file._get_name()
#         fd = open('%s/%s' % (MEDIA_ROOT, str(path) + str(filename)), 'wb' )
#         for chunk in file.chunks():
#                 fd.write(chunk)
#         fd.close()