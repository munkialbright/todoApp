from django.contrib import admin
from django.urls import path, include
from task import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tasks', views.tasks, name='tasks'),
    path('statusupdate/<str:slug>', views.statusupdate, name='statusupdate'),
    path('deletetask/<str:slug>', views.deletetask, name='deletetask'),
    path('search', views.search, name='search')
]
