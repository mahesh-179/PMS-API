from .models import Project
from .serializers import ProjectSerializer
from rest_framework import viewsets
from django.contrib.auth.models import User
from .permissions import IsProjectOwner
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsProjectOwner]