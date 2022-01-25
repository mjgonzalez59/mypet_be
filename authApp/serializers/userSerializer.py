from rest_framework import serializers
from authApp.models.userModel import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'name', 'email', 'phone', 'position']



