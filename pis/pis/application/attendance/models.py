from django.db import models

# Create your models here.
class Attendance(models.Model):
	lec_name = models.CharField("Lecture Name",max_length = 30)
	lec_date = models.DateField("Lecture Date")
	F_name = models.ForeignKey("faculty.faculty",on_delete=models.CASCADE,verbose_name="Faculty Name")
	student_id = models.ForeignKey("student.Student",on_delete=models.CASCADE,verbose_name="Student Id")
	Attendance = models.CharField(
		max_length = 1,
		choices = (
			('P',"Present"),
			('A',"Absent"),
			)
		)
class Meta:
	verbose_name = "Attendance"