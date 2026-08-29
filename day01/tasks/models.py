from django.db import models
from django.contrib.auth.models import User
from projects.models import Project
# Create your models here.
def generate_attachement_path(instance, filename):
    return f'tasks/{instance.created_user.username}/{filename}'
class Task(models.Model):
    class StatusOption(models.TextChoices):
        PENDING = 'PN','Pending'
        COMPLETED = 'CM','Completed'
        CANCELLED = 'C','Cancelled'
        INPROGRESS = 'I','In Progress'
    class PriorityOption(models.TextChoices):
        HIGH = 'H','High'
        MEDIUM = 'M','Medium'
        LOW = 'L','Low'
    title = models.CharField(max_length=100)
    description = models.TextField()
    project_name = models.ForeignKey(Project, related_name='tasks', on_delete=models.CASCADE)
    created_user = models.ForeignKey(User, related_name='created_tasks', on_delete=models.CASCADE)
    assigned_to = models.ManyToManyField(User, related_name='assigned_tasks')
    status = models.CharField(max_length=2, choices=StatusOption.choices, default=StatusOption.PENDING)
    priority = models.CharField(max_length=1, choices=PriorityOption.choices, default=PriorityOption.HIGH)
    start_date = models.DateField()
    due_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    attachment = models.FileField(upload_to=generate_attachement_path, null=True, blank=True)

    def __str__(self):
        return self.title