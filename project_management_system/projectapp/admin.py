from django.contrib import admin
from .models import Document, Notification


@admin.register(Document)

class DocumentAdmin(admin.ModelAdmin):
    list_display=['file', 'upload_time', 'timeviewed', 'title']
    list_filter=['upload_time', 'timeviewed']


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display=['supervisor', 'student','message', 'is_read', 'created_at']