from django.contrib import admin
from .models import ContactUs
# Register your models here.
class AdminViewContactUs(admin.ModelAdmin):
    list_display = ['First_name','Last_name','Email','Mobile','Subject','Messages']
    search_fields = ['First_name','Email']


admin.site.register(ContactUs,AdminViewContactUs)
