import factory

from product.models import Product


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product
