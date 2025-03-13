from django.db import models

# Create your models here.
class Branch(models.Model):
	Branch_name = models.CharField("Branch name",max_length = 30)
	Branch_code = models.CharField("Branch code",max_length = 30)
