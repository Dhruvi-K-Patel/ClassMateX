from django.db import models

# Create your models here.

class Fees(models.Model):
	Branch = models.ForeignKey("branch.Branch",on_delete=models.CASCADE,verbose_name="Branch")
	Fees = models.CharField("Fees",max_length = 20)
	semster = models.CharField(

		max_length = 1,
		choices = (
			("1","1"),
			("2","2"),
			("3","3"),
			("4","4"),
			("5","5"),
			("6","6"),
			("7","7"),
			("8","8"),
			)

		)

class Meta:
	verbose_name = "Fees"