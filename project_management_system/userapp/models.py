from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify
import uuid
from django.conf import settings

# Create your models here.
class CustomUser(AbstractUser):
    ROLE_CHOICES=[
       ( 'student', 'Student'),
        ('supervisor', 'Supervisor'),
    ]
    role= models.CharField(max_length= 20, choices= ROLE_CHOICES )
    name=models.CharField(max_length=50, null=True)
    staff_id= models.CharField(max_length=20, null=True, blank=True)
    matric_number= models.CharField(max_length=20, null=True, blank=True)
    department= models.CharField(max_length= 30, null=True, blank=True)
    email= models.EmailField(unique=True)

    supervisor= models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete= models.SET_NULL,
        limit_choices_to= {'role':'supervisor'},
        related_name= 'students'
    )
    # owner= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.get_full_name
    def get_id(self):
        return f"{self.matric_number or self.staff_id}"
    @property #allows to access full_name as an attribute instead of as a method
    def get_full_name(self):
        return self.name or f"{self.first_name} {self.last_name}".strip()

    def save(self, *args, **kwargs):
        if not self.username:
            if self.name:
                base_username = slugify(self.name)

            else:
                base_username= 'user'

            unique_username=f"{base_username}-{uuid.uuid4().hex[:6]}"
            self.username= unique_username


        super().save(*args, **kwargs)