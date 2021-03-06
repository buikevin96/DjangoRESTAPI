# Defines all the field that would be accessible through the API 
# and how the fields are presented

from .models import Task
from rest_framework import serializers# Import serializers from rest framework

class TaskSerializers(serializers.ModelSerializer):
    
    image = serializers.ImageField(max_length = None, use_url = True) # Define image field
    class Meta:
        # Model serializer belongs to
        model = Task
        fields = ('id', 'task_name', 'task_desc', 'completed', 'date_created', 'image')