from django.db import models

# Create your models here.

class Student(models.Model):
	first_name = models.CharField("First Name",max_length = 30)
	last_name = models.CharField("Last Name",max_length = 30)
	email = models.EmailField("Email Id")
	mobile = models.CharField("Mobile No.",max_length = 10)
	a_number = models.CharField("Alt Number",max_length = 10)
	state_name = models.ForeignKey("locality.State",on_delete=models.CASCADE,verbose_name="State name")
	city = models.ForeignKey("locality.City",on_delete=models.CASCADE,verbose_name="City")
	area = models.ForeignKey("locality.Area",on_delete=models.CASCADE,verbose_name="Area")
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

class Meta:
	verbose_name = "Student"
