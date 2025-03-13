from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	mobile = models.CharField("Mobile No.",max_length = 10)
	a_number = models.CharField("Alt Number",max_length = 10)
	state_name = models.ForeignKey("locality.State",on_delete=models.CASCADE,verbose_name="State name")
	city = models.ForeignKey("locality.City",on_delete=models.CASCADE,verbose_name="City")
	area = models.ForeignKey("locality.Area",on_delete=models.CASCADE,verbose_name="Area")
	departments = models.ForeignKey("departments.departments",on_delete=models.CASCADE,verbose_name="Departments")
	Profile_pic = models.ImageField(upload_to = "studentimages")
	Gender = models.CharField(
		max_length = 1,
		choices = (
			('M',"Male"),
			('F',"Female"),
			('O',"Other"),
			)
		)
	Roll_number = models.IntegerField("Roll number")

	Address = models.TextField("Address")
	DoB = models.DateField("Date of Birth")

	def __unicode__(self):
		return self.user.username

	def __str__(self):
		return self.user.first_name + " " + self.user.last_name


	def get_full_name(self):
		return self.user.first_name + "  " + self.user.last_name
	
	
	

