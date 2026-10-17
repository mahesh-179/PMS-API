
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from api.routers import router as user_router
from projects.routers import router as project_router
from tasks.routers import router as task_router
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
#homepage
from django.http import JsonResponse

def home(request):
    return JsonResponse({
        "message": "Welcome to PMS-API",
        "status": "success",
        "description": (
            "Project Management System API is running successfully."
        ),
        "version": "1.0.0",
        "available_endpoints": {
            "users": "/api/users/",
            "projects": "/api/projects/",
            "tasks": "/api/tasks/",
            "obtain_token": "/api/auth/token/",
            "refresh_token": "/api/auth/token/refresh/",
            "admin": "/admin/"
        },
        "documentation": (
            "Explore the source code on GitHub."
        ),
        "github": "https://github.com/mahesh-179/PMS-API"
    })

#urls new
auth_urlpatterns = [
    path(r'verify/', include('rest_framework.urls')),
]
    
api_urlpatterns = [
    path('auth/token/', TokenObtainPairView.as_view()),
    path('auth/token/refresh/', TokenRefreshView.as_view()),
    path('users/', include(user_router.urls)),
    path('projects/', include(project_router.urls)),
    path('tasks/', include(task_router.urls)),
]
urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('api/', include(api_urlpatterns)),
]+auth_urlpatterns
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



