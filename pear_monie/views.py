from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password, check_password
from rest_framework_simplejwt.tokens import RefreshToken

from pear_monie.models import Customers
from pear_monie.serializer import CustomerRegistrationSerializer
from rest_framework.decorators import api_view


def get_token_for_app_users(users):
    """Generate JWT access & refresh token for authenticated users"""
    refreshToken = RefreshToken.for_user(users)
    return (
        {'refresh': str(refreshToken),
         'access': str(refreshToken.access_token), })
@api_view(['POST'])
def registerCustomer(customerRegisterRequest):
    email = customerRegisterRequest.get['email']
    if not email:
        return Response({'Error: Invalid email'}, status=status.HTTP_400_BAD_REQUEST)
    validate_email_is_taken(email)
    serializer = CustomerRegistrationSerializer(data=customerRegisterRequest.data)
    if serializer.is_valid():
        customer = Customers.objects.create(
            first_name=validate_customer_first_name(serializer.validated_data['first_name']),
            last_name=validate_customer_last_name(serializer.validated_data['last_name']),
            phone_number=validate_customer_phone_number(serializer.validated_data['phone_number']),
            password=make_password(serializer.validated_data['password'])
        )
        app_token = get_token_for_app_users(customer)
        return Response(
            {"customer": CustomerRegistrationSerializer(customer).data, "token": app_token},
            status=status.HTTP_201_CREATED
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
def validate_email_is_taken(email):
    if Customers.objects.filter(email=email).exists():
        raise ValueError("Email already exists")
def validate_customer_phone_number(phone_number):
    if Customers.objects.filter(phone_number=phone_number).exists():
        raise ValueError("Phone number already exists")

    if not phone_number and phone_number is None:
        raise ValueError("Phone number is required")

def validate_customer_first_name(first_name):
    if not first_name and first_name is None:
        raise ValueError("First name is required")

def validate_customer_last_name(last_name):
    if not last_name and last_name is None:
        raise ValueError("Last name is required")

@api_view(['POST'])
def loginCustomers(customerLoginData):
    user_id = customerLoginData.get['id'],
    email = customerLoginData.get['email'],
    password = customerLoginData.get['password']

    if not user_id or not email or not password:
        return Response({"error": "User ID, email, and password are required"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        customer = Customers.objects.get(id=user_id)
    except Customers.DoesNotExist:
        return Response({"error": "User with this ID does not exist"}, status=status.HTTP_400_BAD_REQUEST)

    if customer.email != email:
        return Response({"error": "Invalid email or password"}, status=status.HTTP_400_BAD_REQUEST)

    if not check_password(password, customer.password):  # Validate hashed password
        return Response({"error": "Invalid email or password"}, status=status.HTTP_400_BAD_REQUEST)

    return Response({"message": "Login successful", "customer_id": customer.id}, status=status.HTTP_200_OK)
