
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from api.routers import router as user_router
from projects.routers import router as project_router
from tasks.routers import router as task_router
#urls new
auth_urlpatterns = [
    path(r'verify/', include('rest_framework.urls')),
]
api_urlpatterns = [
    path('users/', include(user_router.urls)),
    path('projects/', include(project_router.urls)),
    path('tasks/', include(task_router.urls)),
]
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_urlpatterns)),
]+auth_urlpatterns
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)