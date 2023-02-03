# shoppingcartapi
Shopping cart API

API to manage Customers, Products and Shopping Carts.

In order to increase the sales amount, the API has a promotional strategy to attract Customers. This promotional strategy for each 3 items added to the cart, the cart will provide a discount equivalent to 1 item. This item being the lowest priced. The analysis for the lowest priced item takes into account the quantity chosen per product.


## Tech details
Developed using django-rest-framework.
Has integration with PostregreSQL.
Tests with pytest.

It has 3 main resources: Customers, Products e ShoppingCarts.

To run the API it's necessary to have docker and docker compose configured in the machine.

With docker and docker compose configured, run the following commands in the root folder of the project:

Build and run postgreSQL and API images:
```
docker compose up -d --build
```
Run migrations:
```
docker compose exec app python manage.py migrate
```

After migrations, the API will be available in localhost on port 8000.

The API documentation Swagger will be available in:

```
http://localhost:8000/
```

Main endpoints:

### Create a customer
```
POST http://localhost:8000/customers

payload = {
    "name": "Customer Name"
}
```

### Create a product
```
POST http://localhost:8000/products

payload = {
    "name": "Dress",
    "price": "20.65"
}
```

### Create a shoppingcart
```
POST http://localhost:8000/shoppingcarts

payload = {
    "customer_id": {customer_id}
}
```

### Add product to shopping cart
```
POST http://localhost:8000/shoppingcarts/{shopping_cart_id}/products/{product_id}

```

### Remove product from shopping cart
```
DELETE http://localhost:8000/shoppingcarts/{shopping_cart_id}/products/{product_id}

```

### Get shopping cart informatioin
Here all information about the shopping cart will be presented, including the total_price.
```
GET http://localhost:8000/shoppingcarts/{shopping_cart_id}
```

API with 94% of test coverage, with tests that validate all the requirements.
