from django.shortcuts import render,redirect,get_object_or_404
from .models import Students

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
        d = request.FILES.get('image')   # use FILES for image
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
    return render(request,'update.html', {'stud':stud})

def uprec(request, id):
    stud = get_object_or_404(Students, id=id)

    if request.method == "POST":
        a = request.POST.get('std_name')
        b = request.POST.get('std_class')
        c = request.POST.get('mobile_number')
        d = request.FILES.get('image')   # use FILES for image
        e = request.POST.get('address')

        stud = Students.objects.get(id=id)
        stud.std_name = a
        stud.std_class = b
        stud.mobile_number = c
        if d:
            stud.image = d
        stud.address = e
        stud.save()
        return redirect('/')
    return render(request, "update.html", {"stud": stud})



