import pytest
from django.urls import reverse
from rest_framework import status
from customer.tests.factories import CustomerFactory
from customer.models import Customer
from customer.serializers import CustomerSerializer


pytestmark = pytest.mark.django_db


def test_create_customer_with_success(client):
    url = reverse("customer:list")
    data = {
        'name': 'Amora'
    }
    response = client.post(url, data=data)

    customer = Customer.objects.get(name='Amora')
    customer_serializer = CustomerSerializer(customer)

    assert response.status_code, status.HTTP_201_CREATED
    assert customer_serializer.data, response.data


def test_patch_customer(client):
    customer = CustomerFactory.create_batch(size=1, name="Raphael")
    url = reverse("customer:detail", kwargs={'pk': customer[0].id})
    data = {
        'name': 'Raphael Nascimento'
    }
    response = client.patch(url, data=data, content_type='application/json')

    filtered_customer = Customer.objects.get(name='Raphael Nascimento')
    customer_serializer = CustomerSerializer(filtered_customer)

    assert response.status_code, status.HTTP_200_OK
    assert customer_serializer.data, response.data


def test_list_customer(client):
    CustomerFactory.create_batch(size=2)
    url = reverse("customer:list")

    response = client.get(url)

    customers = Customer.objects.all()
    customers_serializer = CustomerSerializer(customers, many=True)

    assert response.status_code, status.HTTP_200_OK
    assert customers_serializer.data, response.data


def test_get_by_customer_id(client):
    customers = CustomerFactory.create_batch(size=2)
    url = reverse("customer:detail", kwargs={'pk': customers[0].id})

    response = client.get(url)

    customer = Customer.objects.get(id=customers[0].id)
    customer_serializer = CustomerSerializer(customer)

    assert response.status_code, status.HTTP_200_OK
    assert customer_serializer.data, response.data


def test_delete_by_customer_id(client):
    customer = CustomerFactory.create_batch(size=1)
    url = reverse("customer:detail", kwargs={'pk': customer[0].id})

    response = client.delete(url)

    filtered_customer = Customer.objects.filter(id=customer[0].id)

    assert response.status_code, status.HTTP_204_NO_CONTENT
    assert not filtered_customer


def test_customer_representation(client):
    customer = CustomerFactory.create_batch(size=1, name="Ana")

    assert f"{customer[0]}", f"Customer: {customer[0].name}-{customer[0].id}"
