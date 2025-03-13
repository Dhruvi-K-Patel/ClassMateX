from django.db import models

# Create your models here.
class ContactUs(models.Model):
	First_name = models.CharField("First_name",max_length = 30)
	Last_name = models.CharField("Last_name",max_length = 30)
	Email = models.EmailField("Email Id")
	Mobile = models.CharField("Mobile",max_length = 10)
	Subject = models.CharField("Subject",max_length = 30)
	Messages = models.TextField("Message")

class Meta:
		verbose_name = "Contact Us"