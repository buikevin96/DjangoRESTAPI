from django.db import models

# Create your models here.

# Database structure for Task Model
class Task(models.Model):
    task_name = models.CharField(max_length = 200) # Name of Task
    task_desc = models.CharField(max_length = 200) # Task Description
    date_created = models.DateTimeField(auto_now = True)# Date task was added
    completed = models.BooleanField(default = False)
    image = models.ImageField(upload_to='Image/', default='Images/None/No-img.jpg') # Adds an image view to our model