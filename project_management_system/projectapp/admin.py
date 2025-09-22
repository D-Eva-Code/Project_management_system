from django.contrib import admin
from .models import Document


@admin.register(Document)

class DocumentAdmin(admin.ModelAdmin):
    list_display=['file', 'upload_time', 'timeviewed', 'title']
    list_filter=['upload_time', 'timeviewed']