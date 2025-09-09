from django.urls import path
from projectapp import views

app_name= 'project'

urlpatterns =[path('home', views.home , name='home'),
]