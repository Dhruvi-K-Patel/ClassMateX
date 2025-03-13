from django.contrib import admin
from .models import Attendance
# Register your models here.
class Att(admin.ModelAdmin):
   # list_display = ['Subject','Faculty','ass_date','due_date','upload','student']
    search_fields = ['Subject']
    #list_filter = ['status']

admin.site.register(Attendance,Att)