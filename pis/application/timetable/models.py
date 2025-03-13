from django.db import models

# Create your models here.
class TimeTable(models.Model):
	Subject_name = models.CharField("Subject name",max_length = 30)
	Sub_code = models.IntegerField("Subject code")
	Day = models.CharField(
		max_length = 1,
		choices = (
			('M',"Mon"),
			('T',"Tue"),
			('W',"Wed"),
			('T',"Thu"),
			('F',"Fri"),
			('S',"Sat"),
			)
		)
	Time = models.TimeField("Time")
	F_name = models.ForeignKey("faculty.faculty",on_delete=models.CASCADE,verbose_name="Faculty Name")
	
class Meta:
	verbose_name = "Time Table"