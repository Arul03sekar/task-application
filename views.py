from django.shortcuts import render,  redirect
from .models import task
from .forms import TaskForm

def task_list(request):
    tasks = task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})

def add_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'task_form.html', {'form': form})

def update_task(request,id):
    tasks = task.objects.get(id=id)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=tasks)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=tasks)
    return render(request, 'task_form.html', {'form': form})

def delete_task(request,id):
    tasks = task.objects.get(id=id)
    
    tasks.delete()
    return redirect('task_list')
    

def filter_priority(request, priority):
    tasks = task.objects.filter(priority=priority)
    return render(request, 'task_list.html', {'tasks': tasks})
