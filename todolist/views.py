#type:ignore

from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Todo

def index(request):
    latest_todo_list = Todo.objects.all()
    context = {
        "latest_todo_list": latest_todo_list
    }
    return render(request, "todolist/index.html", context=context)

def create(request):
    new_todo = Todo()
    
    new_todo.title = request.POST["title"]
    new_todo.status = 'DO'
    
    new_todo.save()

    return HttpResponseRedirect(reverse("todos:index"))

def update(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)

    if (request.method == "POST"):
        todo.title = request.POST["title"]
        todo.save()
        return HttpResponseRedirect(reverse("todos:index"))

    return render(request, "todolist/update.html", context={"todo": todo})

def delete(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    todo.delete()
    return HttpResponseRedirect(reverse("todos:index"))

def detail(request, todo_id):
    try:
        todo = Todo.objects.get(pk=todo_id)
    except Todo.DoesNotExist:
        raise Http404("Todo does not exist")
    
    return render(request, "todolist/detail.html", {"todo": todo})

def recap(request):
    todos = Todo.objects.all()
    
    return render(request, "todolist/recap.html", {"todos": todos})

def update_status(request, todo_id):
    try:
        todo = Todo.objects.get(pk=todo_id)
    except Todo.DoesNotExist:
        raise Http404("Todo does not exist")
    
    todo.status = request.POST['status']
    todo.save()

    return HttpResponseRedirect(reverse("todos:index"))