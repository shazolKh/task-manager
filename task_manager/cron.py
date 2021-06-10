from .models import *


def my_scheduled_job():
    Task.objects.create(
        task_name='cron test',
        status='pending',
        additional_info='adddd',
    )
