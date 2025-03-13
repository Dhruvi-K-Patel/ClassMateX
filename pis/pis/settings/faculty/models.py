from django.db import models


class faculty(models.Model):
	first_name = models.CharField("First Name",max_length = 30)
	last_name = models.CharField("Last Name",max_length = 30)
	email = models.EmailField("Email Id")
	Profile_pic = models.ImageField(upload_to = "facultyimages")
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

