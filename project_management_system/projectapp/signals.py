from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Document
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

@receiver(post_save, sender=Document)
def notify_supervisor_on_upload(sender, instance, created, **kwargs):
    
    if created  and  instance.student:
        channel_layer = get_channel_layer()
        supervisor = instance.supervisor
        group_name =  f"supervisor_{supervisor.id}"# Notify the specific supervisor 
        event={
                'type': 'file_uploaded',
                'message': 'New Upload',
                'document_id': instance.id,
                'student_id': instance.student.id
            }
        async_to_sync(channel_layer.group_send)(group_name,event)