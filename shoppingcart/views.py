from rest_framework import viewsets
from rest_framework.mixins import ListModelMixin
from shoppingcartapi.viewsets import CommonModelViewSet
from shoppingcart.models import ShoppingCart, ShoppingCartProduct
from shoppingcart.serializers import ShoppingCartSerializer, ShoppingCartProductSerializer
from product.models import Product
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class ShopppingCartViewSet(viewsets.GenericViewSet, CommonModelViewSet):
    serializer_class = ShoppingCartSerializer
    filterset_fields = ['customer_id',]

    def get_queryset(self):
        queryset = ShoppingCart.objects.all()
        pk = self.kwargs.get('pk')
        if pk is not None:
            queryset = ShoppingCart.objects.filter(id=pk)
        return queryset


class ShopppingCartProductViewSet(viewsets.GenericViewSet, ListModelMixin):
    serializer_class = ShoppingCartProductSerializer

    def list(self, request, shopping_cart_id, **kwargs):
        self.queryset = ShoppingCartProduct.objects.filter(shoppingcart__id=shopping_cart_id)

        return super().list(request)

    def add(self, request, shopping_cart_id, product_id, **kwargs):
        shopping_cart = get_object_or_404(ShoppingCart, id=shopping_cart_id)
        product = get_object_or_404(Product, id=product_id)

        if shopping_cart_product := shopping_cart.shoppingcartproduct.filter(product__id=product_id):
            shopping_cart_product.update(
                quantity=shopping_cart_product[0].quantity + 1
            )
        else:
            ShoppingCartProduct.objects.create(
                shoppingcart=shopping_cart,
                product=product,
                quantity=1,
            )

        self.serializer_class = ShoppingCartSerializer
        self.queryset = ShoppingCart.objects.filter(id=shopping_cart_id)
        return super().list(request)

    def remove(self, request, shopping_cart_id, product_id, **kwargs):
        shopping_cart = get_object_or_404(ShoppingCart, id=shopping_cart_id)
        get_object_or_404(Product, id=product_id)

        if shopping_cart_product := shopping_cart.shoppingcartproduct.filter(product__id=product_id):
            if shopping_cart_product[0].quantity > 1:
                shopping_cart_product.update(
                    quantity=shopping_cart_product[0].quantity - 1
                )
            else:
                shopping_cart_product[0].delete()

        self.serializer_class = ShoppingCartSerializer
        self.queryset = ShoppingCart.objects.filter(id=shopping_cart_id)
        return super().list(request)
