from django.shortcuts import render
from .models import Students

def index(request):
    stud=Students.objects.all()
    return render(request,'index.html',{'stud':stud})