from django.db import models

# Create your models here.
class departments(models.Model):
    Name = models.CharField(max_length=150)
    departments_info = models.TextField(default="")
    status = models.BooleanField(default=False)


    def __str__(self):
    	return self.Name