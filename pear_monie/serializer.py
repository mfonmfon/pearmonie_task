from django.contrib.auth import authenticate
from rest_framework import serializers
from models import Customers


class CustomerRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'password']

class CustomerLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = ['id','email', 'password']
class ContentSerializer(serializers.Serializer):
    class Meta:
        fields = ['title', 'description']
