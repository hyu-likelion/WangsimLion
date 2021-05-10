from django.shortcuts import render, get_object_or_404, redirect
from .models import to_do
# Create your views here.

def home(request):
    todos=to_do.objects
    return render(request, 'home.html', {'to_dos':todos})

def create(request):
    todos=to_do()
    todos.title = request.GET['title']
    todos.save()
    return redirect('home', new_todos.id)

def edit(request, todos_id):
    edit_todos=to_do.objects.get(id=todos_id)
    return render(request, 'edit.html', {'to_dos':edit_todos})


def update(request, todos_id):
    update_todos = to_do.objects.get(id=todos_id)
    update_todos.title = request.GET['title']
    update_todos.save()
    return redirect ('home')



def delete(request, todos_id):
    delete_todos = to_do.objects.get(id=todos_id)
    delete_todos.delete()
    return redirect('home')