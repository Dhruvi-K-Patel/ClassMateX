from django.contrib import admin
from .models import TimeTable
# Register your models here.


class AdminViewTimeTable(admin.ModelAdmin):
    list_display = ['Subject_name','Sub_code','Day','Time','F_name']
    search_fields = ['Subject_name']


admin.site.register(TimeTable,AdminViewTimeTable)
