from django.db import models
from django.contrib.auth.models import User

class faculty(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	Profile_pic = models.ImageField(upload_to = "facultyimages")
	About_faculty = models.TextField(default="")
	state_name = models.ForeignKey("locality.State",on_delete=models.CASCADE,verbose_name="Sate name")
	city = models.ForeignKey("locality.City",on_delete=models.CASCADE,verbose_name="City")
	area = models.ForeignKey("locality.Area",on_delete=models.CASCADE,verbose_name="Area")
	Gender = models.CharField(
		max_length = 1,
		choices = (
			('M',"Male"),
			('F',"Female"),
			('O',"Other"),
			)
		)
	Exp = models.CharField("Experience",max_length = 15)
	qua = models.CharField("Qualification",max_length = 30)
	dep = models.CharField("Department",max_length = 15)
	Mobileno = models.CharField("Mobile Number",max_length = 10)
	DoB = models.DateField("Date of Birth")

	class Meta:
		verbose_name = "Faculty"

	def __str__(self):
		return self.user.first_name 
