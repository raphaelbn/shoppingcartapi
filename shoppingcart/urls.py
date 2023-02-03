from django.urls import re_path

from shoppingcart.views import ShopppingCartViewSet, ShopppingCartProductViewSet


urlpatterns = [
    re_path(
        r'^/?$', 
        ShopppingCartViewSet.as_view({'post': 'create','get': 'list'}), 
        name='list',
    ),
    re_path(
        r'^/(?P<pk>\d+)/?$', 
        ShopppingCartViewSet.as_view({'get': 'retrieve', 'delete': 'destroy'}), 
        name='shoppingcart-detail',
    ),
    re_path(
        r'^/(?P<shopping_cart_id>\d+)/products/?$', 
        ShopppingCartProductViewSet.as_view({'get': 'list'}), 
        name='list_products',
    ),
    re_path(
        r'^/(?P<shopping_cart_id>\d+)/products/(?P<product_id>\d+)/?$', 
        ShopppingCartProductViewSet.as_view({'post': 'add', 'delete': 'remove'}), 
        name='add_remove',
    ),
]
