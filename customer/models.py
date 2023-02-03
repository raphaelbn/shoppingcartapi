from django.db import models
from shoppingcartapi.models import TimesTampedModel


class Customer(TimesTampedModel):
    name = models.CharField(max_length=150)

    def __str__(self):
        return f'Customer: {self.name}-{self.id}'
