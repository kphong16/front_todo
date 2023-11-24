# todo/urls.py

from django.urls import path
from . import views
urlpatterns = [
    path('todos/', views.todo_list, name='todo_list'),
    path('todo/<int:pk>/', views.todo_detail, name='todo_detail'),
    path('add_todo/', views.add_todo, name='add_todo'),
    path('completed_todos/', views.completed_todos, name='completed_todos'),
    path('edit_todo/', views.edit_todo, name='edit_todo'),
]
