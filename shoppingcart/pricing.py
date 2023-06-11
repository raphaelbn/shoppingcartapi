from shoppingcart.models import ShoppingCart
from abc import ABC
from decimal import Decimal


class Pricing(ABC):
    def calculate(shoppingcart: ShoppingCart) -> Decimal:
        pass


class PromotionalPricing(Pricing):
    def calculate(shoppingcart: ShoppingCart) -> Decimal:
        total_itens = shoppingcart.total_itens
        if not total_itens:
            return Decimal("0.0")

        itens_to_discount = total_itens // 3
        total_discount = 0
        for shoppingcartproduct in sorted(shoppingcart.shoppingcartproduct.all(), key=lambda item: item.product.price):
            if shoppingcartproduct.quantity < itens_to_discount:
                total_discount += (shoppingcartproduct.product.price * shoppingcartproduct.quantity)
                itens_to_discount -= shoppingcartproduct.quantity
            else:
                total_discount += (shoppingcartproduct.product.price * itens_to_discount)
                break

        return Decimal(shoppingcart.total_price - total_discount)
