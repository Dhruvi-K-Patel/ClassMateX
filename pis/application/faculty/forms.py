from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import faculty
from django.contrib.auth.models import User
from timetable.models import TimeTable
from student.models import Student
from ebook.models import Ebook
from attendance.models import Attendance
from assignment.models import Assignment

class UserForm(forms.ModelForm):
        class Meta:
                model = User
                fields = ["username", "email", "password","first_name","last_name"]




class AddAssignment(forms.ModelForm):
        class Meta:
                model = Assignment
                fields = '__all__'
                

class UserProfileForm(forms.ModelForm):
        class Meta:
                model = faculty
                fields = '__all__'
                exclude = ['user']


class AttendanceForm(forms.ModelForm):
        class Meta:
                model = Attendance
                fields = '__all__'
                exclude = ['']


class EbookAdd(forms.ModelForm):
        class Meta:
                model = Ebook
                fields = '__all__'
                exclude = ['']


class TimeTableForm(forms.ModelForm):
	class Meta:
		model = TimeTable
		fields = '__all__'
		exclude = ['F_name']