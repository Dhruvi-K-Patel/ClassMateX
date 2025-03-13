from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Student
from django.contrib.auth.models import User
from assignment.models import Assignment


class UserForm(forms.ModelForm):
        class Meta:
                model = User
                fields = ["username", "email", "password","first_name","last_name"]



class UserProfileForm(forms.ModelForm):
        class Meta:
                model = Student
                fields = '__all__'
                exclude = ['user']



class AssignmentForm(forms.ModelForm):
	class Meta:
		model = Assignment
		fields = '__all__'
		exclude = ['']
