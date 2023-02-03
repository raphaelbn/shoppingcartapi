from django.db import models
from shoppingcartapi.models import TimesTampedModel


class Product(TimesTampedModel):
    name = models.CharField(max_length=50)
    price = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return f'Product: {self.name}-{self.id}'
