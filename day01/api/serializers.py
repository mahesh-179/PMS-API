from .models import Student
from django.contrib.auth.models import User
from rest_framework import serializers

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    profile = StudentSerializer(read_only=True)
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password','profile']
