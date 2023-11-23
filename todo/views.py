# todo/views.py
from django.shortcuts import render, redirect
from django.urls import reverse
import requests

# Create your views here.
def todo_list(request):
    return render(request, 'todo/todo_list.html')

def completed_todos(request):
    return render(request, 'todo/completed_todos.html')

def todo_detail(request, pk):
    return render(request, 'todo/todo_detail.html')

def add_todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')

        response = requests.post('http://127.0.0.1:8000/todo/', json={'title':title, 'description':description})
        if response.status_code == 201:
            return redirect(reverse('todo_list'))
    return render(request, 'todo/add_todo.html')
