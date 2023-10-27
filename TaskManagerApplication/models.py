# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField()
    status = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20)
