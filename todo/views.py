# todo/views.py
from django.shortcuts import render

# Create your views here.
def todo_list(request):
    return render(request, 'todo/todo_list.html', {})
