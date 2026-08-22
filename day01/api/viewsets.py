from rest_framework.viewsets import ModelViewSet
from .serializers import UserSerializer,StudentSerializer
from .models import Student
from django.contrib.auth.models import User
class StudentAPI(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class UserAPI(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
