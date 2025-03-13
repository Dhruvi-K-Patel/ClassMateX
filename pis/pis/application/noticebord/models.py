from django.db import models

# Create your models here.
class NoticeBoard(models.Model):
	Date = models.DateField()
	Title = models.CharField("Title",max_length = 150)
	Type = models.CharField(
		max_length = 1,
		choices = (
			('E',"Educational"),
			('S',"Seminar"),
			('W',"Workshop"),
			('C',"Curriculum Activity"),
			('A',"Admission process"),
			('E',"Exam"),
			('R',"Result"),
			)
		)
	F_name = models.ForeignKey("faculty.faculty",on_delete=models.CASCADE,verbose_name="Faculty name")
	HOD_name = models.ForeignKey("Hod.Hod",on_delete=models.CASCADE,verbose_name="Hod name")
	status = models.BooleanField("Status",default = False)

class Meta:
	verbose_name = "NoticeBoard"