from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Task(models.Model):
    # created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=255)
    STATUS_TYPE = (
        ('complete', 'Complete'),
        ('incomplete', 'Incomplete'),
        ('outstanding', 'Outstanding'),
        ('no_status', 'No Status'),
    )
    status = models.CharField(max_length=255, choices=STATUS_TYPE, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    additional_info = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.task_name}'
