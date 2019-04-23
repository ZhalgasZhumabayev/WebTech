from django.contrib import admin
from django.urls import path, include
from .views import TaskList_list, TaskList_detail, Task_List, Task_detail

urlpatterns = [
    path('task_list/', TaskList_list),
    path('task_list/<int:pk>', TaskList_detail),
    path('task_list/<int:pk>/tasks/', Task_List),
    path('tasks/<int:pk>/', Task_detail)
]
