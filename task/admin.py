from django.contrib import admin
from .models import *


@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ("user_login", "upload_datetime", "image", "history")
