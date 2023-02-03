import factory

from customer.models import Customer


class CustomerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Customer
