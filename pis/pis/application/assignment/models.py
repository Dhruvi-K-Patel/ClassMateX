from django.db import models

# Create your models here.
class Assignment(models.Model):
	Subject = models.CharField("Subject",max_length = 100)
	Faculty = models.ForeignKey("faculty.faculty",on_delete=models.CASCADE,verbose_name="Faculty")
	ass_date = models.DateField("Assign Date")
	due_date = models.DateField("Due Date")
	upload = models.FileField(upload_to = "studentassignment/")
	Student = models.ForeignKey("student.Student",on_delete=models.CASCADE,verbose_name="Student")
class Meta:
	verbose_name = "Assignment"