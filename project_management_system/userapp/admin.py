from django.contrib import admin
from userapp.models import CustomUser
# Register your models here.
@admin.register(CustomUser)

class CustomUserAdmin(admin.ModelAdmin):
    list_display= ['username', 'name', 'role', 'get_id', 'department', 'supervisor']
    list_filter= ['role', 'department']
    search_fields= ['username', 'staff_id', 'matric_number']