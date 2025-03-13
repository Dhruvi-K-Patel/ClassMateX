from django.db import models

# Create your models here.

class Canteen(models.Model):
	Food_item = models.CharField("Food item",max_length = 30)	
	Price = models.CharField("Price",max_length = 30)
class Meta:
		verbose_name = "Canteen"