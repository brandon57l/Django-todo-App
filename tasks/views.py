from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from .filters import *

# Create your views here.

def home(request):
    tasks = Task.objects.all()
    form = TaskForm()
   

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    filter = TaskFilter(request.GET, queryset=tasks)
    tasks = filter.qs
    
    context = {'tasks':tasks, 'form':form, 'filter':filter}

    return render(request, 'list.html', context)

def updateTask(request, id):
    task = Task.objects.get(id=id)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form':form}

    return render(request, 'update_task.html', context)

def deleteTask(request, id):
    task = Task.objects.get(id=id)


    if request.method == 'POST':
        task.delete()
        return redirect('home')

    context = {'task':task}

    return render(request, 'delete_task.html', context)

