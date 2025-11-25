from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Document(models.Model):
    file= models.FileField(upload_to='documents/%Y/%m/%d')
    upload_time= models.DateTimeField(auto_now_add= True)
    title= models.CharField(max_length=40, default='Project Document')
    description= models.CharField(max_length=200, null=True, blank=True)
   
    
    STATUS_CHOICES=[
        ('submitted', 'Submitted'),
        ('in_review', 'In Review'),
        ('not_approved', 'Not Approved'),
        ('approved', 'Approved')
    ]

    status= models.CharField(max_length= 20, choices= STATUS_CHOICES, default='submitted')
    timeviewed= models.DateTimeField(auto_now= True)
    supervisor= models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete= models.CASCADE,
        related_name= 'documents'
    )
    # student= models.ForeignKey(
    #     settings.AUTH_USER_MODEL,
    #     null=True,
    #     blank=True,
    #     on_delete= models.CASCADE,
    #     related_name= 'supervised_students'
    # )
    owner= models.ForeignKey(settings.AUTH_USER_MODEL,null=True,blank=True,on_delete= models.CASCADE)
    def __str__(self):
        return self.title
    class Meta:
        ordering= ['-upload_time']


class Notification(models.Model):
    supervisor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notifications')
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='upload_notifications')
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)

    # def __str__(self):
    #     return f"Notification for {self.supervisor.get_full_name()} from {self.student.get_full_name()}"

    