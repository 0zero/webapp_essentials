"""
This module contains the tests for the product API endpoints.
"""


def test_create_product(test_app):
    # Create a new product
    product_data = {
        "name": "Test Product",
        "description": "This is a test product",
        "price": 9.99,
    }
    response = test_app.post("/products/", json=product_data)
    assert response.status_code == 201
    assert response.json()["name"] == product_data["name"]
    assert response.json()["description"] == product_data["description"]
    assert response.json()["price"] == product_data["price"]


def test_get_product_by_name(test_app):
    # Retrieve a product by its name
    product_name = "Test Product"
    response = test_app.get(f"/products/{product_name}")
    assert response.status_code == 200
    assert response.json()["name"] == product_name


def test_get_all_products(test_app):
    # Retrieve all products
    response = test_app.get("/products/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_update_product(test_app):
    # Update a product by its name
    product_name = "Test Product"
    updated_product_data = {
        "description": "This is an updated test product",
        "price": 19.99,
    }
    response = test_app.put(f"/products/{product_name}", json=updated_product_data)
    assert response.status_code == 201
    assert response.json()["name"] == product_name
    assert response.json()["description"] == updated_product_data["description"]
    assert response.json()["price"] == updated_product_data["price"]


def test_delete_product(test_app):
    # Delete a product by its name
    product_name = "Test Product"
    response = test_app.delete(f"/products/{product_name}")
    assert response.status_code == 200
    assert response.json()["name"] == product_name
