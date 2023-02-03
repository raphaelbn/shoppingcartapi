from django.urls import re_path

from product.views import ProductViewSet


urlpatterns = [
    re_path(
        r'^/?$', 
        ProductViewSet.as_view({'post': 'create','get': 'list'}), 
        name='list',
    ),
    re_path(
        r'^/(?P<pk>\d+)/?$', 
        ProductViewSet.as_view({'get': 'retrieve', 'delete': 'destroy', 'patch': 'partial_update'}), 
        name='detail',
    ),
]
