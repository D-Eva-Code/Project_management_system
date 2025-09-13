from django.urls import path
from projectapp import views

app_name= 'project'

urlpatterns =[
    path('supervisor/dashboard', views.supervisor , name='supervisor_dashboard'),
    path('student/dashboard', views.student, name='student_dashboard'),

]