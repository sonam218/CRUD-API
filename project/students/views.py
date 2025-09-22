from django.shortcuts import render,redirect,get_object_or_404
from .models import Students
import os
from django.contrib import messages

def index(request):
    stud=Students.objects.all()
    return render(request,'index.html',{'stud':stud})

def add(request):
    return render(request,'add.html')

def addrec(request):
    if request.method == "POST":
        a = request.POST.get('std_name')
        b = request.POST.get('std_class')
        c = request.POST.get('mobile_number')
        d = request.FILES.get('image')
        e = request.POST.get('address')

        student = Students(
            std_name=a,
            std_class=b,
            mobile_number=c,
            image=d,
            address=e
        )
        student.save()
        return redirect('/')

def delete(request, id):
    stud=Students.objects.get(id=id)
    stud.delete()
    return redirect("/")

def update(request,id):
    stud=Students.objects.get(id=id)

    if request.method=="POST":
        stud.std_name=request.POST.get('std_name') 
        stud.std_class=request.POST.get('std_class')
        stud.mobile_number=request.POST.get('mobile_number')
        stud.address=request.POST.get('address')
         # Handle image update
        if len(request.FILES) != 0:
            if len(stud.image) > 0:
                if stud.image:
                    if os.path.isfile(stud.image.path):
                        os.remove(stud.image.path)
                    stud.image =request.FILES['image']
                else:
                    stud.image =request.FILES['image']
        stud.save()
        messages.success(request, "Student updated successfully.")
        return redirect('/')
    return render(request, "update.html", {"stud": stud})



