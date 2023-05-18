from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile


# Create a serializer for the user profile:
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'
