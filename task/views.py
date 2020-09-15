from django.shortcuts import render, HttpResponse, redirect
from task.models import Task
from django.db.models import Q

# Create your views here.
def home(request):
    context = {'successful': '', 'unsuccessful': ''}

    if request.method == "POST":
        #Handle the task form
        title = request.POST['title']
        desc = request.POST['desc']
        start_time = request.POST['start_time']
        deadline = request.POST['deadline']

        #print(title, desc)
        if Task.objects.filter(task_title=title):
            context = {'unsuccessful': 'Task already exist with same title. Please change title'}
        else:
            task = Task(task_title = title, task_description = desc, start_time = start_time, deadline = deadline)
            task.save()
            context = {'successful': 'The task was successfully created.', 'title': title}
    
    return render(request, 'index.html', context)

def tasks(request):
    activeTasks = Task.objects.filter(status='active')
    inactiveTasks = Task.objects.filter(status='inactive')
    #for item in allTasks:
    #    print(item.taskTitle)
    context = {'tasks': activeTasks, 'untasks': inactiveTasks}
    return render(request, 'tasks.html', context)

def statusupdate(request, slug):
    task = Task.objects.filter(Q(task_title=slug) & Q(status='active'))
    if task:
        task.update(status='inactive')
    else:
        Task.objects.filter(Q(task_title=slug) & Q(status='inactive')).update(status='active')
    return redirect('tasks')

def deletetask(request, slug):
    Task.objects.get(Q(task_title=slug)).delete()
    return redirect('tasks')

def search(request):
    if request.method == 'GET':
        srch = request.GET.get('search')
        tasks = Task.objects.filter(Q(task_title__icontains=srch))
        context = {'tasks': tasks, 'srch_input': srch}
    return render(request, 'search.html', context)
