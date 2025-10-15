from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from userapp.models import CustomUser
from django.conf import settings
from .forms import UploadForm
from .models import Document
from django.contrib import messages
from django.urls import reverse
# Create your views here.
@login_required
def student(request):
    if request.user.role != "student":
        return redirect('project:supervisordashboard', supervisor_id=request.user.id)
    if request.user.is_authenticated:
        
        full_name=request.user.get_full_name
        if request.method=="POST":
            form= UploadForm(request.POST, request.FILES)
            if form.is_valid():
                # new_form= Document(file= request.FILES['file'])
                new_form= form.save(commit=False)
                new_form.owner= request.user
                new_form.supervisor= request.user.supervisor
                new_form.save()
                messages.success(request, "File Successfully Uploaded")
        else:
            form= UploadForm()
        return render(request, 'student_dashboard.html',{"full_name":full_name, "form":form})
    


@login_required
def supervisor(request, supervisor_id):
    # return HttpResponse("Home page")
    if request.user.role != "supervisor":
        return redirect("project:studentdashboard")
    else:
     
        full_name= request.user.get_full_name if request.user.is_authenticated else ""
        supervisor = CustomUser.objects.get(id=supervisor_id, role='supervisor')
        students = supervisor.students.all()  # reverse relation
    return render(request, 'supervisor_dashboard.html', {"full_name":full_name, 'students': students,'supervisor':supervisor})

@login_required
def projectupload(request):
    if request.user.is_authenticated:
       loop_form= Document.objects.filter(owner=request.user)
    else:
        loop_form= Document.objects.none()

    return render(request, "project.html", {"loop_form":loop_form})

@login_required
def supervisor_students(request, supervisor_id):
    supervisor = CustomUser.objects.get(id=supervisor_id, role='supervisor')
    students = supervisor.students.all()  # reverse relation
    return render(request, 'supervisor_dashboard.html', {'supervisor': supervisor, 'students': students})

@login_required
def student_projects(request, student_id):
    student = CustomUser.objects.get(id=student_id, role='student')
    projects= Document.objects.filter(owner=student)
    return render(request, 'student_projects.html', {'student':student, 'projects': projects})

@login_required
def delete_file(request, file_id):
    file = Document.objects.get(id=file_id)
    if file.owner == request.user:
        file.delete()
    else:
        messages.error("Access restricted")
    return redirect('project:projectupload')

@login_required
def search_view(request):
    searchfield = request.GET.get('q')
    result=[]
    if searchfield:
        result= Document.objects.filter(title__icontains=searchfield).distinct()
    else:
        result= Document.objects.all()
    return render(request, 'project.html', {'result':result, 'searchfield':searchfield})

@login_required
def update_project_status(request, document_id):
    document= Document.objects.get(id=document_id)
    # if request.user== document.supervisor:
    if request.user.id == document.supervisor.id:
        if request.method=="POST":
            new_status= request.POST.get("status")
            document.status= new_status
            document.save()
            return redirect('project:supervisordashboard', supervisor_id=request.user.id)

    return render(request, 'supervisor_dashboard.html', {"document":document})