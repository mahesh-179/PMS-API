from django.db import models
from django.contrib.auth.models import User
def generateimage(instance,file):
    return f"images/profile/{instance.user.username}/{file}"
class Profile(models.Model):
    class RoleOption(models.TextChoices):
        Employer = 'E','Employer'
        Worker = 'W','Worker'
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name="profile")
    first_name = models.CharField(max_length=15)
    middle_name = models.CharField(max_length=15,null=True,blank=True)
    last_name = models.CharField(max_length=15)
    address = models.TextField()
    profile_image = models.ImageField(upload_to=generateimage)
    role = models.CharField(max_length=1,choices=RoleOption.choices,default=RoleOption.Worker)

    def __str__(self):
        return f"{self.first_name}-{self.last_name}"

