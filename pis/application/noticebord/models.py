from django.db import models

# Create your models here.
class NoticeBoard(models.Model):
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
	NoticeBoardimage = models.ImageField(upload_to="NoticeBoardimage/")
	status = models.BooleanField("Status",default = False)

class Meta:
	verbose_name = "NoticeBoard"