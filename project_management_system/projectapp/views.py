from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from userapp.models import CustomUser
from django.conf import settings

# Create your views here.
@login_required
def student(request):
    if request.user.is_authenticated:
        # author=CustomUser.objects.filter(owner=request.user)
        full_name=request.user.get_full_name
        return render(request, 'student_dashboard.html',{"full_name":full_name})
    else:
        return render(request, "login.html")


@login_required
def supervisor(request):
    # return HttpResponse("Home page")
    full_name= request.user.get_full_name if request.user.is_authenticated else ""
    return render(request, 'supervisor_dashboard.html', {"full_name":full_name})