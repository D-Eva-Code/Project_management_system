from django.db import models

# Create your models here.
class Document(models.Model):
    file= models.FileField(upload_to='documents/%Y/%m/%d')
    upload_time= models.DateTimeField(auto_now_add= True)
    status= models.CharField()
    
