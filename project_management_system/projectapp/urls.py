from django.urls import path
from projectapp import views

app_name= 'project'

urlpatterns =[
    path('supervisor/<int:supervisor_id>/dashboard/', views.supervisor , name='supervisordashboard'),
    path('student/dashboard', views.student, name='studentdashboard'),
    path('student/projectuploads', views.projectupload, name= 'projectupload'),
    path('supervisor/update_status/<int:document_id>/', views.update_project_status, name='update_project_status'),
    path('supervisor/<int:supervisor_id>/students/', views.supervisor_students, name='supervisor_students'),
    path('supervisor/student/<int:student_id>/projects/', views.student_projects, name='student_projects'),
    path('student/<int:file_id>/', views.delete_file, name='delete_projects'),
    path('student/search/', views.search_view, name='search'),
    path('student/searchstudent/', views.search_student, name='searchname'),
]