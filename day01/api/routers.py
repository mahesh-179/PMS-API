from rest_framework.routers import DefaultRouter
from .viewsets import ProfileAPI,UserAPI
from django.urls import path, include
router = DefaultRouter()
router.register("profiles/",ProfileAPI)
router.register("users/",UserAPI)
