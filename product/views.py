from rest_framework import viewsets
from shoppingcartapi.viewsets import CommonModelViewSet
from product.models import Product
from product.serializers import ProductSerializer


class ProductViewSet(viewsets.GenericViewSet, CommonModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
