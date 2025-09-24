from django.db import models
from django.conf import settings

# Create your models here.
class Document(models.Model):
    file= models.FileField(upload_to='documents/%Y/%m/%d')
    upload_time= models.DateTimeField(auto_now_add= True)
    title= models.CharField(max_length=40)
   
    

#     def __str__(self):
#         return self.file

# class SupervisorFeedback(models.Model):
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
        null=True,
        blank=True,
        on_delete= models.SET_NULL,
        related_name= 'students_supervisor'
    )
    student= models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete= models.CASCADE,
        related_name= 'supervised_students'
    )
    owner= models.ForeignKey(settings.AUTH_USER_MODEL,null=True,blank=True,on_delete= models.CASCADE)

    def __str__(self):
        return self.title