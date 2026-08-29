from django.contrib import admin
from .models import Task
# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'project_name', 'created_user', 'status', 'priority', 'start_date', 'due_date', 'created_at', 'updated_at')
    list_filter = ('status', 'priority', 'start_date', 'due_date')
    search_fields = ('title', 'description', 'project_name__title', 'created_user__username')
    ordering = ('-created_at',)

admin.site.register(Task, TaskAdmin)