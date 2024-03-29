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
        ('no status', 'No Status'),
        ('pending', 'Pending'),
    )
    status = models.CharField(max_length=255, choices=STATUS_TYPE, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    additional_info = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.task_name}'


class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    details = models.TextField()
    commented_at = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return f'Commented on {self.task.task_name} by {self.user}'


class ApprovalRequest(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=255, null=True, blank=True)
    approved = models.BooleanField(default=False)
