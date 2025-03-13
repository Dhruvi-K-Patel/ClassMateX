from django.db import models

# Create your models here.
class Ebook(models.Model):
	Book_name = models.CharField("Book name",max_length = 30)
	author_name = models.CharField("Author name",max_length = 30)
	Book_image = models.ImageField(upload_to = "Book_image/")
	Edition = models.CharField("Edition",max_length= 30)
	Subject_name = models.CharField("Subject name",max_length = 10)
	review = models.CharField("Review",max_length  = 30)
	upload_pdf = models.FileField(upload_to = "uploadBook/")
	
	class Meta:
		verbose_name = "Ebook"