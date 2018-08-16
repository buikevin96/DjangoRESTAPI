from django.shortcuts import render
from rest_framework import viewsets # Import rest framework viewsets
from .serializers import TaskSerializers # Import taskSerializers from serializers.py
from .models import Task # Import Task from models.py

# Create your views here.

# Define view for particular API
class TaskViewSet(viewsets.ModelViewSet): # Inherits from 

    # Extract data from the task model
    queryset = Task.objects.all().order_by('-date_created')
    serializer_class = TaskSerializers # Class to use with the view