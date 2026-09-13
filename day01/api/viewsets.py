from rest_framework.viewsets import ModelViewSet
from .serializers import ProfileSerializer, UserSerializer
from .models import Profile
from .permissions import *
from django.contrib.auth.models import User
class ProfileAPI(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsProfileUserOrGetProfile]


class UserAPI(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsUserOwnerOrGetPost]  # Apply the custom permission class
