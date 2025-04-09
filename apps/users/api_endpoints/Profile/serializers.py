from django.db import models
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()



class ProfileSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(required=True)  
    profile_picture = serializers.ImageField(required=False)  
    region = serializers.CharField(required=True)  
    phone_number = serializers.CharField(required=True) 
    email = serializers.EmailField(required=True)  
    
    
    class Meta:
        model = User
        fields = ("full_name","profile_picture","region","phone_number","email")



