from django.contrib.auth import authenticate
from rest_framework import serializers
from models import Customers


class CustomerRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'password']

    # def validate_email(self, data):
    #     """Check if email already exists"""
    #     if Customers.objects.filter(email=data.email).exists():
    #         raise serializers.ValidationError("Email already exists")
    #     return data

    # def create(self, customer_data):
    #     """Create a user to the platform"""
    #     customers = Customers.objects.create(
    #         first_name=customer_data['first_name'],
    #         last_name=customer_data['last_name'],
    #         email=customer_data['email'],
    #         phone_number=customer_data['phone_number'],
    #     )
    #     customers.set_password(customer_data['password'])
    #     customers.save()
    #     return customers


class CustomerLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = ['id','email', 'password']

class ContentSerializer(serializers.Serializer):
    class Meta:
        fields = ['title', 'description']
