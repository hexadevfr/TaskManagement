from django.db import models
from django.forms import ModelForm
from django.conf import settings

# Create your models here.

class Task(models.Model):
    utilisateur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    finished = models.BooleanField(default=False)

    def __str__(self):
        return self.title



class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields =['title', 'description', 'finished']
