from decimal import Decimal
from django.db import models
from django.core.validators import MinValueValidator
from product.models import Product
from customer.models import Customer
from shoppingcartapi.models import TimesTampedModel


class ShoppingCart(TimesTampedModel):
    class StatusChoices(models.TextChoices):
        OPENED = 'opened', 'Opened'
        CLOSED = 'closed', 'Closed'
        PAID = 'paid', 'Paid'

    customer = models.ForeignKey(Customer, related_name='shoppingcart', on_delete=models.CASCADE)
    status = models.CharField(max_length=6, choices=StatusChoices.choices, default=StatusChoices.OPENED)

    @property
    def total_itens(self) -> int:
        if not self.shoppingcartproduct.all():
            return 0

        total_itens = 0
        for shoppingcartproduct in self.shoppingcartproduct.all():
            total_itens += shoppingcartproduct.quantity
        return total_itens

    @property
    def total_price(self) -> Decimal:
        if not self.shoppingcartproduct.all():
            return 0

        price = 0
        for shoppingcartproduct in self.shoppingcartproduct.all():
            price += (shoppingcartproduct.quantity * shoppingcartproduct.product.price)
        return price

    def __str__(self):
        return f'ShoppingCart: {self.id}'


class ShoppingCartProduct(TimesTampedModel):
    shoppingcart = models.ForeignKey(ShoppingCart, related_name='shoppingcartproduct', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='shoppingcartproduct', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1, validators=[MinValueValidator(1)])

    @property
    def item_price(self):
        return self.product.price * self.quantity
