from django.shortcuts import render
from rest_framework import viewsets # Import rest framework viewsets
from .serializers import TaskSerializers # Import taskSerializers from serializers.py
from .models import Task # Import Task from models.py

# Create your views here.

# Define view for particular API
class TaskViewSet(viewsets.ModelViewSet): 

    # Extract data from the task model
    queryset = Task.objects.all().order_by('-date_created')
    serializer_class = TaskSerializers # Class to use with the view

class DueTaskViewSet(viewsets.ModelViewSet):

    queryset = Task.objects.order_by('-date_created').filter(completed = False)
    serializer_class = TaskSerializers

class CompletedTaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.order_by('-date_created').filter(completed = True)
    serializer_class = TaskSerializers