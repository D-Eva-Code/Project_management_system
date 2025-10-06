from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Document
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

@receiver(post_save, sender=Document)
def notify_supervisor_on_upload(sender, instance, created, **kwargs):
    print(f"--- Signal Triggered for Document ID: {instance.id} ---")
    print(f"Created: {created}")
    print(f"Has Owner: {bool(instance.owner)}")
    print(f"Has Supervisor: {bool(instance.supervisor)}")
    print("Sending to group: supervisor_", instance.supervisor.id)
    print(" Supervisor username:", instance.supervisor.username)

    if created  and  instance.owner and instance.supervisor:
        print(f"--- Signal Fired: Notifying supervisor {instance.supervisor.id} ---")
        channel_layer = get_channel_layer()
        supervisor = instance.supervisor
        group_name =  f"supervisor_{supervisor.id}"# Notify the specific supervisor 
        print(f"Sending to group: {group_name}")
        event={
                'type': 'file_uploaded',
                'message': 'New Upload!',
                # 'document_id': instance.id,
                'owner_id': instance.owner.id
            }
        async_to_sync(channel_layer.group_send)(group_name,event)