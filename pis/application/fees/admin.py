from django.contrib import admin
from .models import Fees
# Register your models here.
class AdminViewFees(admin.ModelAdmin):
    list_display = ['Branch','Fees','semster']
    search_fields = ['Branch']


admin.site.register(Fees,AdminViewFees)