from django.db import models

# Create your models here.

class Feedback(models.Model):
	First_name = models.CharField("First name",max_length = 30)
	Last_name = models.CharField("Last name",max_length = 30)
	Email = models.EmailField("Email ID")
	Mobile = models.CharField("Mobile",max_length = 10)
	Subject = models.CharField("Subject",max_length = 30)
	Messages = models.TextField("Messages")
	Rating = models.IntegerField("Rating")

class Meta:
		verbose_name = "Feedback"