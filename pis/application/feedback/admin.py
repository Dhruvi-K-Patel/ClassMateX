from django.contrib import admin
from .models import Feedback
# Register your models here.

class AdminViewFeedback(admin.ModelAdmin):
    list_display = ['First_name','Last_name','Email','Mobile','Subject','Messages','Rating']
    search_fields = ['First_name','Email']


admin.site.register(Feedback,AdminViewFeedback)