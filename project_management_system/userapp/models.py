from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    ROLE_CHOICES=[
       ( 'student', 'Student'),
        ('supervisor', 'Supervisor'),
    ]
    role= models.CharField(max_length= 20, choices= ROLE_CHOICES )

    staff_id= models.CharField(max_length=20, null=True)
    matric_number= models.CharField(max_length=20, null=True)
    department= models.CharField(max_length= 30, null=True)

    supervisor= models.ForeignKey(
        'self',
        null=True,
        on_delete= models.SET_NULL,
        limit_choices_to= {'role':'supervisor'},
        related_name= 'students'
    )