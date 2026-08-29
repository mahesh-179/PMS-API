from django.urls import path,include
from .routers import router

urlpatterns = [
    path("tasks/",include(router.urls))
]
