from django.db import models

# Create your models here.
class Result(models.Model):
	Branch = models.ForeignKey("branch.Branch",on_delete=models.CASCADE,verbose_name="Branch")
	Student = models.ForeignKey("student.Student",on_delete=models.CASCADE,verbose_name="Stuadent")
	exam_type = models.CharField(
		max_length = 3,
		choices = (
			("M","Mid"),
			("O","Other"),
			)

		)
	o_mark = models.IntegerField("Obtained Mark ")
	total_mark = models.IntegerField("Total Mark")
	ex_date = models.DateField("Exam Date")

class Meta:
	verbose_name = "Result"