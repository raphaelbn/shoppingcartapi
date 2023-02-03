from rest_framework import viewsets
from shoppingcartapi.viewsets import CommonModelViewSet
from customer.models import Customer
from customer.serializers import CustomerSerializer


class CustomerViewSet(viewsets.GenericViewSet, CommonModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
