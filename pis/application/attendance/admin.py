from django.contrib import admin
from .models import Attendance
# Register your models here.
class Att(admin.ModelAdmin):
    list_display = ['lec_name','lec_date','F_name','student_id','Attendance']
    search_fields = ['Subject','lec_name']
    #list_filter = ['status']

admin.site.register(Attendance,Att)