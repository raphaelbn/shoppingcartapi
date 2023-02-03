from django.urls import re_path

from customer.views import CustomerViewSet


urlpatterns = [
    re_path(
        r'^/?$', 
        CustomerViewSet.as_view({'post': 'create','get': 'list'}), 
        name='list',
    ),
    re_path(
        r'^/(?P<pk>\d+)/?$', 
        CustomerViewSet.as_view({'get': 'retrieve', 'delete': 'destroy', 'patch': 'partial_update'}), 
        name='detail',
    ),
]
