import pytest
from decimal import Decimal
from customer.tests.factories import CustomerFactory
from shoppingcart.tests.factories import ShoppingCartFactory, ShoppingCartProductFactory
from product.tests.factories import ProductFactory


@pytest.fixture
def default_customer():
    return CustomerFactory.create_batch(size=1, name="Raphael")[0]


@pytest.fixture
def default_product():
    return ProductFactory.create_batch(size=1, name='product_test', price=Decimal('15.99'))[0]


@pytest.fixture
def default_shoppingcart(default_customer):
    return ShoppingCartFactory.create_batch(size=1, customer=default_customer)[0]


@pytest.fixture
def shoppingcart_with_1_product(default_shoppingcart, default_product):
    ShoppingCartProductFactory.create_batch(size=1, shoppingcart=default_shoppingcart, product=default_product, quantity=1)[0]
    return default_shoppingcart


@pytest.fixture
def shoppingcart_with_3_tshirts(default_shoppingcart):
    tshirt = ProductFactory.create_batch(size=1, name='t-shirt', price=Decimal('12.99'))[0]
    ShoppingCartProductFactory.create_batch(size=1, shoppingcart=default_shoppingcart, product=tshirt, quantity=3)[0]
    return default_shoppingcart


@pytest.fixture
def shoppingcart_with_2_tshirts_2_jeans(default_shoppingcart):
    tshirt = ProductFactory.create_batch(size=1, name='t-shirt', price=Decimal('12.99'))[0]
    jeans = ProductFactory.create_batch(size=1, name='jeans', price=Decimal('25.00'))[0]
    ShoppingCartProductFactory.create_batch(size=1, shoppingcart=default_shoppingcart, product=tshirt, quantity=2)[0]
    ShoppingCartProductFactory.create_batch(size=1, shoppingcart=default_shoppingcart, product=jeans, quantity=2)[0]
    return default_shoppingcart


@pytest.fixture
def shoppingcart_with_1_tshirt_2_jeans_3_dress(default_shoppingcart):
    tshirt = ProductFactory.create_batch(size=1, name='t-shirt', price=Decimal('12.99'))[0]
    jeans = ProductFactory.create_batch(size=1, name='jeans', price=Decimal('25.00'))[0]
    dress = ProductFactory.create_batch(size=1, name='dress', price=Decimal('20.65'))[0]
    ShoppingCartProductFactory.create_batch(size=1, shoppingcart=default_shoppingcart, product=tshirt, quantity=1)[0]
    ShoppingCartProductFactory.create_batch(size=1, shoppingcart=default_shoppingcart, product=jeans, quantity=2)[0]
    ShoppingCartProductFactory.create_batch(size=1, shoppingcart=default_shoppingcart, product=dress, quantity=3)[0]
    return default_shoppingcart
