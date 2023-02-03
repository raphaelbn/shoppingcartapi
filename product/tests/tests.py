import pytest
from decimal import Decimal
from django.urls import reverse
from rest_framework import status
from product.tests.factories import ProductFactory
from product.models import Product
from product.serializers import ProductSerializer


pytestmark = pytest.mark.django_db


def test_create_product_with_success(client):
    url = reverse('product:list')
    data = {
        'name': 'T-shirt',
        'price': Decimal('12.99')
    }
    response = client.post(url, data=data)

    product = Product.objects.get(name='T-shirt')
    product_serializer = ProductSerializer(product)

    assert response.status_code, status.HTTP_201_CREATED
    assert product_serializer.data, response.data


def test_patch_product(client):
    product = ProductFactory.create_batch(size=1, name='Jeans', price=Decimal('20.00'))
    url = reverse('product:detail', kwargs={'pk': product[0].id})
    data = {
        'price': '25.00'
    }
    response = client.patch(url, data=data, content_type='application/json')

    filtered_product = Product.objects.get(name='Jeans')
    product_serializer = ProductSerializer(filtered_product)

    assert response.status_code, status.HTTP_200_OK
    assert product_serializer.data, response.data


def test_list_product(client):
    ProductFactory.create_batch(size=2, name='Product tests', price=Decimal('19.00'))
    url = reverse('product:list')

    response = client.get(url)

    products = Product.objects.all()
    products_serializer = ProductSerializer(products, many=True)

    assert response.status_code, status.HTTP_200_OK
    assert products_serializer.data, response.data


def test_get_by_product_id(client):
    products = ProductFactory.create_batch(size=2, name='Product tests', price=Decimal('19.00'))
    url = reverse("product:detail", kwargs={'pk': products[0].id})

    response = client.get(url)

    product = Product.objects.get(id=products[0].id)
    product_serializer = ProductSerializer(product)

    assert response.status_code, status.HTTP_200_OK
    assert product_serializer.data, response.data


def test_delete_by_product_id(client):
    product = ProductFactory.create_batch(size=1, name='Product tests', price=Decimal('19.00'))
    url = reverse("product:detail", kwargs={'pk': product[0].id})

    response = client.delete(url)

    filtered_product = Product.objects.filter(id=product[0].id)

    assert response.status_code, status.HTTP_204_NO_CONTENT
    assert not filtered_product


def test_product_representation(client):
    product = ProductFactory.create_batch(size=2, name='Product tests', price=Decimal('19.00'))

    assert f"{product[0]}", f"Product: {product[0].name}-{product[0].id}"
