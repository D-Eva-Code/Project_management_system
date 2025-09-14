from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def student(request):
    # return HttpResponse("Home page")
    return render(request, 'student_dashboard.html')
@login_required
def supervisor(request):
    # return HttpResponse("Home page")
    full_name= request.user.get_full_name if request.user.is_authenticated else ""
    return render(request, 'supervisor_dashboard.html', {"full_name":full_name})