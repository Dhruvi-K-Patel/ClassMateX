from django.contrib import admin
from .models import Lab
# Register your models here.

class AdminViewLab(admin.ModelAdmin):
    list_display = ['Subject','Practical_name','Student','status']
    search_fields = ['Subject']


admin.site.register(Lab,AdminViewLab)
