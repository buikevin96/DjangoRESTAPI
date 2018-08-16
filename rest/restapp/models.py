from django.db import models

# Create your models here.

# Database structure for Task Model
class Task(models.Model):
    task_name = models.CharField(max_length = 200) # Name of Task
    task_desc = models.CharField(max_length = 200) # Task Description
    date_created = models.DateTimeField(auto_now = True)# Date task was added
    