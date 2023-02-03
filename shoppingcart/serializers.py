from rest_framework import serializers
from shoppingcart.models import ShoppingCart, ShoppingCartProduct
from product.serializers import ProductListSerializer
from shoppingcart.pricing import PromotionalPricing


class ShoppingCartProductSerializer(serializers.ModelSerializer):
    product = ProductListSerializer()

    class Meta:
        model = ShoppingCartProduct
        fields = ('product', 'quantity')


class ShoppingCartSerializer(serializers.ModelSerializer):
    customer_id = serializers.IntegerField()
    shoppingcartproduct = ShoppingCartProductSerializer(many=True, required=False)
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = ShoppingCart
        fields = ('id', 'created_at', 'updated_at', 'customer_id', 'status', 'shoppingcartproduct', 'total_price')

    def get_total_price(self, shoppingcart):
        return PromotionalPricing.calculate(shoppingcart)
