from django.urls import path
from . import views
# from django.contrib.auth import views as auth_views

urlpatterns=[
    path('register/', views.register, name='register'),
    path('login/', views.RoleBasedLoginView.as_view(template_name= 'login.html'), name='login'),
]