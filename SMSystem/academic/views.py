from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentsDataForm
from .models import Student, Subject
from django.contrib import messages
# Create your views here.
def homepage(request,):
    if request.method == 'POST':
        std = StudentsDataForm(request.POST)
        if std.is_valid():
            std.save()
            messages.success(request,'Data Added Succesfully')
    else:
        std = StudentsDataForm()
    st = Student.objects.all()
    ss = Subject.objects.all()
    return render(request, 'academic/data.html', {'std':std, 'st':st, 'cg':ss })

def update(request, id):
    if request.method == 'POST':
        pi = Student.objects.get(pk=id)
        fm = StudentsDataForm(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Succesfully Updated')
            return HttpResponseRedirect('/')
    else:
        pi = Student.objects.get(pk=id)
        fm = StudentsDataForm(instance=pi)
    return render(request, 'academic/update.html', {'fm':fm})

def delete(request, id):
    if request.method == 'POST':
        pi = Student.objects.get(pk=id)
        pi.delete()
        messages.success(request,'Succesfully Deleted')
        return HttpResponseRedirect('/')
