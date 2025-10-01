# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from .models import Document

# @receiver(post_save, sender=Document)
# def notify_supervisor_on_upload(sender, instance, created, **kwargs):
#     if created and instance.supervisor:

#         supervisor= instance.supervisor
#         student= instance.owner
#         print(f"Notification: {supervisor.get_full_name}, your student {student.get_full_name} has uploaded a new document titled '{instance.title}'.")