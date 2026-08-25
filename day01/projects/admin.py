from django.contrib import admin
from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'created_user',
        'status',
        'priority',
        'created_at',
        'updated_at',
    )

    list_filter = (
        'status',
        'priority',
        'created_at',
        'updated_at',
    )

    search_fields = (
        'title',
        'description',
        'created_user__username',
        'assigned_to__username',
    )

    filter_horizontal = ('assigned_to',)

    readonly_fields = (
        'created_at',
        'updated_at',
    )