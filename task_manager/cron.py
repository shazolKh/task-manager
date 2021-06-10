from .models import *

def my_scheduled_job():
    Task.objects.update(status='no status')
