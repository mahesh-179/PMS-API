from rest_framework import serializers
from .models import Task
from projects.serializers import ProjectSerializer
class TaskSerializer(serializers.ModelSerializer):
    created_user = serializers.HyperlinkedRelatedField(view_name='user-detail', many=False, read_only=True)
    assigned_to = serializers.HyperlinkedRelatedField(view_name='user-detail', many=True, read_only=True)
    project_name = ProjectSerializer(read_only=True)
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'project_name', 'created_user', 'assigned_to', 'status', 'priority', 'start_date', 'due_date', 'created_at', 'updated_at']