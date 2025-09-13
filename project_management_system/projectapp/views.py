from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.
def student(request):
    # return HttpResponse("Home page")
    return render(request, 'student_dashboard.html')

def supervisor(request):
    # return HttpResponse("Home page")
    return render(request, 'supervisor_dashboard.html')