from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_task, name='list_task'),
    path('new/', views.new_task, name='new_task'),
    path('edit/<int:pk>/', views.edit_task, name='edit_task'),
    path('delete/<int:pk>/', views.delete_task, name='delete_task')
]