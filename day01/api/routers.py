from rest_framework.routers import DefaultRouter
from .viewsets import StudentAPI,UserAPI
router = DefaultRouter()
router.register('students',StudentAPI)
router.register('user',UserAPI)

