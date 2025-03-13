from django.contrib import admin
from .models import *
# Register your models here.
class AdminViewDepartment(admin.ModelAdmin):
    list_display = ['Name','departments_info','status']
    search_fields = ['Name']


admin.site.register(departments,AdminViewDepartment)
