from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Task, TaskForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
# Create your views here.

class InscriptionView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'inscription.html'


@login_required
def list_task(request):
    task = Task.objects.all()
    return render(request, 'task/list_task.html', {'task':task})


def new_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('list_task'))
    else:
        form = TaskForm()
    return render(request, 'Task/new_task.html', {'form' : form})


def edit_task(request, pk):
    task = Task.objects.get(pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect(reverse('list_task'))
    else:
        form = TaskForm(instance=task)
    return render(request, 'Task/edit_task.html', {'form' : form})


def delete_task(request, pk):
    Task.objects.get(pk=pk).delete()
    return HttpResponseRedirect(reverse('list_task'))