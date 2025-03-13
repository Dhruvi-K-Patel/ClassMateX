from django.db import models

# Create your models here.
class Hostel(models.Model):
	Hostel_name = models.CharField("Hostel name",max_length = 30)
	mobile = models.CharField("Mobile",max_length = 10)
	email = models.EmailField("Email")
	fees = models.CharField("Fees",max_length = 3)
	address  = models.TextField("Address")
	status = models.BooleanField("Status",default = False)
	
class Meta:
		verbose_name = "Hostel Details"