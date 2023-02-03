from django.contrib import admin
from shoppingcart.models import ShoppingCart


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ('id',)
    list_filter = ('id',)
    search_fields = ('id',)
