from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class Customers(AbstractUser):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Subscriptions(models.Model):
    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE)
    subscription_type = models.CharField(max_length=20)
    subscription_price = models.DecimalField(max_digits=10, decimal_places=2)
    subscription_start_date = models.DateTimeField(null=True)
    subscription_end_date = models.DateTimeField(null=True)
    auto_renewal = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.subscription_type} {self.customer}"


class Content(models.Model):
    id = models.AutoField(primary_key=True)
    content_title = models.CharField(max_length=20)
    content_description = models.TextField(max_length=102)
    time_stamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.content_description} {self.content_title}"