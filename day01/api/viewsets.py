from rest_framework.viewsets import ModelViewSet
from .serializers import ProfileSerializer, UserSerializer
from .models import Profile
from django.contrib.auth.models import User
class ProfileAPI(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class UserAPI(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
