from .models import Profile
from django.contrib.auth.models import User
from rest_framework import serializers

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['url','first_name','middle_name','last_name','address','role','profile_image']

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        user = instance 
        if 'password' in validated_data:
            password = validated_data.pop('password')
            user.set_password(password)
            user.save()
            return user
        
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password','profile']
