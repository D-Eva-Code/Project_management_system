from django.urls import path
from projectapp import views

app_name= 'project'

urlpatterns =[
    path('supervisor/dashboard', views.supervisor , name='supervisordashboard'),
    path('student/dashboard', views.student, name='studentdashboard'),
]