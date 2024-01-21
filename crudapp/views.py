from django.shortcuts import render,redirect
from crudapp.models import Student

# Create your views here.
def index(request):
    return render(request,'index.html')

def save(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        mail = request.POST.get('mail')
        age = request.POST.get('age')
        Student.objects.create(name=name,address=address,mail=mail,age=age)
        return redirect('display')
    else:
        return redirect('display')

def display(request):
    students = Student.objects.all()
    return render(request,'display.html',{'students':students})

def update(request,pk):
    student = Student.objects.get(id=pk)
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        mail = request.POST.get('mail')
        age = request.POST.get('age')

        student.name = name
        student.address = address
        student.mail = mail
        student.age = age

        student.save()
        return redirect('display')
    else:
        return render(request,'update.html',{'student':student})

def delete(request,pk):
    student = Student.objects.get(id=pk)
    student.delete()
    return redirect('display')



