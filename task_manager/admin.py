from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    model = Task
    list_display = (
        'task_name',
        'status',
        'updated_at',
        'updated_by',
    )
