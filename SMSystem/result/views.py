from django.shortcuts import render, HttpResponseRedirect
from academic.models import Student, Subject
from django.contrib import messages

# Create your views here.
def addresult(request, id):
    if request.method == 'POST':
        pi = Student.objects.get(pk=id)
        a = int(request.POST.get('a'))
        b = request.POST.get('b')
        aa = int(request.POST.get('aa'))
        bb = request.POST.get('bb')
        aaa = int(request.POST.get('aaa'))
        bbb = request.POST.get('bbb')
        d = a+aa+aaa
        if d>=240:
            d = 'A+'
        elif d>=200:
            d = 'A'
        elif d>=180:
            d = 'A-'
        elif d>=150:
            d = 'B'
        elif d>=120:
            d = 'C'
        elif d>=100:
            d = 'D'
        else:
            d = 'F'
        result = Subject(std=pi, gpa=d, sub_name_1=b, sub_number1=a,sub_name_2=bb, sub_number2=aa,sub_name_3=bbb, sub_number3=aaa)
        result.save()
        messages.success(request,'Result Added Succesfully')
    pi = Student.objects.get(pk=id)
    return render(request, 'result/resadd.html',{'p':pi})

def showresult(request, id):
    if request.method == 'GET':
        pi = Student.objects.get(pk=id)
        try:
            ps = Subject.objects.get(std=id)
        except Subject.DoesNotExist:
            ps = None
    else:
        pi = Student.objects.get(pk=id)
        ps= Subject.objects.get(std=id)
    return render(request, 'result/showresult.html',{'s':pi, 'ps':ps} )

def detailsres(request, id):
    if request.method == 'GET':
        pi = Student.objects.get(pk=id)
        try:
            ps = Subject.objects.get(std=id)
        except Subject.DoesNotExist:
            ps = None
    else:
        ps= Subject.objects.get(std=id)
        pi = Student.objects.get(pk=id)
    return render(request, 'result/detailsres.html', {'s':pi, 'ps':ps})











