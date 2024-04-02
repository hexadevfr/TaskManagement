from django.shortcuts import render
from .models import Task
# Create your views here.

def list_task(request):
    task = Task.objects.all()
    return render(request, 'task/list_task.html', {'task':task})