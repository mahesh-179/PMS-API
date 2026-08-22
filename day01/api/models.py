from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=15)
    middle_name = models.CharField(max_length=15,null=True,blank=True)
    last_name = models.CharField(max_length=15)
    address = models.TextField()
    grade_choice=[
        ('B','Bachelor'),
        ('M','Master')
    ]
    grade = models.CharField(choices=grade_choice,max_length=1)


    def __str__(self):
        return f"{self.first_name}-{self.last_name}"

