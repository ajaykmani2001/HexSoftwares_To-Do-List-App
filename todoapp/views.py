from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *

# Create your views here.

def index(request):
    return render(request,'index.html')

def addtodo(request):
    if(request.method == 'POST'):
        title=request.POST.get('title')
        description=request.POST.get('description')
        db=Todo(title=title,description=description)
        db.save()
        return HttpResponse("to do added")
    return render(request,'addtodo.html')


def displaytodo(request):
    db=Todo.objects.all()
    return render(request,'viewtodo.html',{'data':db})





def remove(request,id):
    db=Todo.objects.get(id=id)
    db.delete()
    return redirect(displaytodo)


def complete(request,id):
    data=Todo.objects.get(id=id)
    data.completed=True
    data.save()
    return redirect(displaytodo)