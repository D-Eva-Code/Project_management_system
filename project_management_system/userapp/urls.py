from django.urls import path
from . import views
from userapp.forms import EmailAuthentication
# from django.contrib.auth import views as auth_views
urlpatterns=[
    path('register/', views.register, name='register'),
    path('login/', views.RoleBasedLoginView.as_view(template_name= 'login.html', authentication_form= EmailAuthentication), name='login'),
    path('logout/', views.log_out, name='logout'),
]