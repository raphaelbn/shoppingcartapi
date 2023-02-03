import pytest
from decimal import Decimal
from django.urls import reverse
from rest_framework import status
from shoppingcart.models import ShoppingCart
from shoppingcart.serializers import ShoppingCartSerializer


pytestmark = pytest.mark.django_db


def test_create_shoppingcart_with_success(client, default_customer):
    url = reverse('shoppingcart:list')
    data = {
        'customer_id': default_customer.id
    }
    response = client.post(url, data=data)

    shoppingcart = ShoppingCart.objects.get(customer_id=default_customer.id)
    shoppingcart_serializer = ShoppingCartSerializer(shoppingcart)

    assert response.status_code, status.HTTP_201_CREATED
    assert shoppingcart_serializer.data, response.data


def test_list_shoppingcarts(client, shoppingcart_with_1_product):
    url = reverse('shoppingcart:list')

    response = client.get(url)

    shoppingcarts = ShoppingCart.objects.all()
    shoppingcarts_serializer = ShoppingCartSerializer(shoppingcarts, many=True)

    assert response.status_code, status.HTTP_200_OK
    assert shoppingcarts_serializer.data, response.data


def test_add_item_to_shoppingcart(client, default_shoppingcart, default_product):
    url = reverse(
        'shoppingcart:add_remove', 
        kwargs={'shopping_cart_id': default_shoppingcart.id, 'product_id': default_product.id},
    )

    response = client.post(url)

    shoppingcart = ShoppingCart.objects.get(id=default_shoppingcart.id)
    shoppingcarts_serializer = ShoppingCartSerializer(shoppingcart)

    assert response.status_code, status.HTTP_200_OK
    assert shoppingcarts_serializer.data, response.data
    assert shoppingcart.total_itens, 1


def test_remove_item_from_shoppingcart(client, shoppingcart_with_1_product):
    url = reverse(
        'shoppingcart:add_remove', 
        kwargs={
            'shopping_cart_id': shoppingcart_with_1_product.id, 
            'product_id': shoppingcart_with_1_product.shoppingcartproduct.first().product.id
        },
    )

    response = client.delete(url)

    shoppingcart = ShoppingCart.objects.get(id=shoppingcart_with_1_product.id)
    shoppingcarts_serializer = ShoppingCartSerializer(shoppingcart)

    assert response.status_code, status.HTTP_200_OK
    assert shoppingcarts_serializer.data, response.data
    assert (shoppingcart.total_itens, 0)
    assert (shoppingcart.total_price, Decimal('0.0'))


def test_check_price_of_shopping_cart_with_3_tshirts(client, shoppingcart_with_3_tshirts):
    url = reverse('shoppingcart:shoppingcart-detail', kwargs={'pk': shoppingcart_with_3_tshirts.id})

    response = client.get(url)

    assert(response.status_code, status.HTTP_200_OK)
    assert(response.data['total_price'], Decimal('25.98'))


def test_check_price_of_shopping_cart_with_2_tshirts_2_jeans(client, shoppingcart_with_2_tshirts_2_jeans):
    url = reverse('shoppingcart:shoppingcart-detail', kwargs={'pk': shoppingcart_with_2_tshirts_2_jeans.id})

    response = client.get(url)

    assert response.status_code, status.HTTP_200_OK
    assert response.data['total_price'], Decimal('62.99')


def test_check_price_of_shopping_cart_with_1_tshirt_2_jeans_3_dress(client, shoppingcart_with_1_tshirt_2_jeans_3_dress):
    url = reverse('shoppingcart:shoppingcart-detail', kwargs={'pk': shoppingcart_with_1_tshirt_2_jeans_3_dress.id})

    response = client.get(url)

    assert response.status_code, status.HTTP_200_OK
    assert response.data['total_price'], Decimal('86.95')


def test_shoppingcart_representation(client, default_shoppingcart):
    assert f"{default_shoppingcart}", f"Product: {default_shoppingcart.name}-{default_shoppingcart.id}"
