from rest_framework.routers import DefaultRouter
from .viewsets import ProfileAPI,UserAPI
router = DefaultRouter()
router.register('profiles',ProfileAPI)
router.register('user',UserAPI)

