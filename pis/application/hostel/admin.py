from django.contrib import admin
from .models import Hostel
# Register your models here.
class AdminViewHostel(admin.ModelAdmin):
    list_display = ['Hostel_name','mobile','email','fees','address','status']
    search_fields = ['Hostel_name']


admin.site.register(Hostel,AdminViewHostel)