from django.contrib import admin
from django.urls import include, path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Shopping Cart API ",
        default_version='v1',
        description="Swagger Shopping Cart API",
        terms_of_service="https://www.ourapp.com/policies/terms/",
        contact=openapi.Contact(email="raphaelbn10@gmail.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('customers', include(('customer.urls', 'customer'), namespace='customer')),
    path('products', include(('product.urls', 'product'), namespace='product')),
    path('shoppingcarts', include(('shoppingcart.urls', 'shoppingcart'), namespace='shoppingcart')),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
