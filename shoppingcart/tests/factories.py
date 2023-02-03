import factory

from shoppingcart.models import ShoppingCart, ShoppingCartProduct
from product.tests.factories import ProductFactory


class ShoppingCartFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ShoppingCart


class ShoppingCartProductFactory(factory.django.DjangoModelFactory):
    shoppingcart = factory.SubFactory(ShoppingCartFactory)
    product = factory.SubFactory(ProductFactory)

    class Meta:
        model = ShoppingCartProduct
