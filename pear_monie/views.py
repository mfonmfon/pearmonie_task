from django.shortcuts import render

from pear_monie.models import Customers


# Create your views here.
class CustomerView:
    def registerCustomer(self, customerRegisterData):
        customers = Customers.objects.create(
            first_name=customerRegisterData.get['first_name'],
            last_name=customerRegisterData.get['last_name'],
            email=customerRegisterData.get['email'],
            phone_number=customerRegisterData.get['phone_number'],
        )
        customers.set_password(customerRegisterData.get['password'])
        customers.save()
        return customers

    def loginCustomers(self, customerLoginData):
        customers = Customers.objects.query(Customers.id).filter(customerLoginData.get['id'])
        email = customerLoginData.get['email']
        if not customerLoginData.get['email']:
            raise ValueError("Invalid email")
        customers.set_password(customerLoginData.get['password'])
        customers.save()
        return customers
