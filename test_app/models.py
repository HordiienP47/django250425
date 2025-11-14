from django.db import models

from model import Models

class Task(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    categories =
    status =
    deadline =
    created_at =

class SubTask(models.Model):
    title =
    description =
    task =
    status =
    deadline =
    created_at =