from django.contrib import admin
from .models import *

# Register your models here.

class AdminViewState(admin.ModelAdmin):
    list_display = ['state_name','status']
    search_fields = ['state_name']

admin.site.register(State,AdminViewState)

class AdminViewCity(admin.ModelAdmin):
    list_display = ['state_name','city_name','status']
    search_fields = ['city_name']
admin.site.register(City,AdminViewCity)

class AdminViewArea(admin.ModelAdmin):
    list_display = ['city_name','area_name','status']
    search_fields = ['area_name']
admin.site.register(Area,AdminViewArea)
