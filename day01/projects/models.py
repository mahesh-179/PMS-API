from django.db import models
from django.contrib.auth.models import User
def Generate_path(instance,file):
    return f"images/projects/{instance.id}/{file}"
class Project(models.Model):
    class StatusOption(models.TextChoices):
        PENDING = 'PN','Pending'
        COMPLETED = 'CM','Completed'
        CANCELLED = 'C','Cancelled'
        INPROGRESS = 'I','In Progress'
    class PriorityOption(models.TextChoices):
        HIGH = 'H','High'
        MEDIUM = 'M','Medium'
        LOW = 'L','Low'
    title = models.TextField(max_length=25)
    description = models.TextField(blank=True,null=True)
    created_user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='created_projects')
    assigned_to = models.ManyToManyField(User,blank=True, related_name='assigned_projects')
    status = models.CharField(max_length=2,choices=StatusOption.choices,default=StatusOption.PENDING)
    priority = models.CharField(max_length=1,choices=PriorityOption.choices,default=PriorityOption.HIGH)
    created_at = models.DateField(auto_now_add=True,editable=False)
    updated_at = models.DateField(auto_now=True,editable=False)
    task_image = models.ImageField(upload_to=Generate_path)

