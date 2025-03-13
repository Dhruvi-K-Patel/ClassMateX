from django.contrib import admin
from .models import Assignment
# Register your models here.
class Ass(admin.ModelAdmin):
    list_display = ['Subject','Faculty','ass_date','due_date','upload','Student']
    search_fields = ['Subject']
    #list_filter = ['status']
    

admin.site.register(Assignment,Ass)
