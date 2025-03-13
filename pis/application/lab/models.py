from django.db import models

# Create your models here.
class Lab(models.Model):
	Subject = models.CharField("Subject",max_length = 30)
	Practical_name = models.CharField("Practical name",max_length = 30)
	Student = models.ForeignKey("student.Student",on_delete=models.CASCADE,verbose_name="Student")
	status = models.BooleanField("Status",default = False)

class Meta:
		verbose_name = "Lab"
	