from .models import Project
from rest_framework import serializers
from django.contrib.auth.models import User
class ProjectSerializer(serializers.ModelSerializer):
    created_user = serializers.HyperlinkedRelatedField(view_name='user-detail', many=False, read_only=True)
    assigned_to = serializers.HyperlinkedRelatedField(view_name='user-detail', many=True, read_only=True)
    class Meta:
        model = Project
        fields = ['id','url','title','description','created_user','assigned_to','status','priority','created_at','updated_at','task_image']