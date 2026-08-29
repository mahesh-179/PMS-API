from rest_framework import routers
from django.urls import path, include
from .viewsets import ProjectViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('projects', ProjectViewSet)