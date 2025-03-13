from django.db import models

# Create your models here.
class State(models.Model):
	state_name = models.CharField("State name",max_length = 30)
	status = models.BooleanField("Status",default=False)

	def __str__(self):
		return self.state_name

class City(models.Model):
	state_name = models.ForeignKey(State,on_delete=models.CASCADE,verbose_name="State name")
	city_name = models.CharField("City name",max_length = 30)
	status = models.BooleanField("Status",default=False)

	def __str__(self):
		return self.city_name

class Area(models.Model):
	city_name = models.ForeignKey(City,on_delete=models.CASCADE,verbose_name="City name")
	area_name = models.CharField("Area name",max_length = 30)
	status = models.BooleanField("Status",default=False)

	def __str__(self):
		return self.area_name	

	class Meta:
		verbose_name = "Locality"