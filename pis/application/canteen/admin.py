from django.contrib import admin
from .models import Canteen
# Register your models here.
class AdminViewCanteen(admin.ModelAdmin):
    list_display = ['Food_item','Price']
    search_fields = ['Food_item']


admin.site.register(Canteen,AdminViewCanteen)
