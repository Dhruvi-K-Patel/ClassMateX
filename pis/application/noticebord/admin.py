from django.contrib import admin
from .models import NoticeBoard
# Register your models here.


class AdminViewNoticeBoard(admin.ModelAdmin):
    search_fields = ['Title']


admin.site.register(NoticeBoard,AdminViewNoticeBoard)