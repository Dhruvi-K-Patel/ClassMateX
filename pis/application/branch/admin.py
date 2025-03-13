from django.contrib import admin
from .models import Branch
# Register your models here.
class AdminViewBranch(admin.ModelAdmin):
    list_display = ['Branch_name','Branch_code']
    search_fields = ['Branch_name']


admin.site.register(Branch,AdminViewBranch)