from .routers import router
from django.urls import path,include

urlpatterns = [
    path("tasks_list/",include(router.urls)),
]