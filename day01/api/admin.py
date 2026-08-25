from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ['first_name','middle_name','last_name','address','grade']

admin.site.register(Student,StudentAdmin)
