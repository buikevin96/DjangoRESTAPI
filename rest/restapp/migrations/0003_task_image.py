# Generated by Django 2.1 on 2018-08-18 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapp', '0002_task_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='image',
            field=models.ImageField(default='Images/None/No-img.jpg', upload_to='Image/'),
        ),
    ]
