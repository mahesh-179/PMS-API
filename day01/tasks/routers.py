from rest_frmework immport routers
from rest_framework.routers import DefaultRouter
from .viewsets import TaskViewSet

router = DefaultRouter()
router.register('tasks', TaskViewSet)