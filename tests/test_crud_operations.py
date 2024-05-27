"""
This module contains tests for the CRUD operations in the database.
"""

import pytest
from src.database.crud_operations import (
    delete_product,
    get_all_products,
    get_product,
    post_product,
    update_product,
)
from src.database.product import Product, ProductUpdate
from pydantic import ValidationError


def test_post_product(test_db):
    # Create a test product
    product = Product(name="Test Product", price=10.99)

    # Add the product to the database
    added_product = post_product(test_db, product)

    # Check if the product was added successfully
    assert added_product.id is not None
    assert added_product.name == "Test Product"
    assert added_product.price == 10.99
    assert added_product.in_stock is False


def test_get_product(test_db):
    # Add a test product to the database
    product = Product(name="Test Product", price=999.99)
    test_db.add(product)
    test_db.commit()

    # Retrieve the product from the database
    retrieved_product = get_product(test_db, "Test Product")

    # Check if the product was retrieved successfully
    assert retrieved_product is not None
    assert retrieved_product.name == "Test Product"
    assert retrieved_product.price == 999.99


def test_get_all_products(test_db):
    # Add some test products to the database
    product1 = Product(name="Product 1", price=9.99)
    product2 = Product(name="Product 2", price=19.99)
    test_db.add_all([product1, product2])
    test_db.commit()

    # Retrieve all products from the database
    products = get_all_products(test_db)

    # Check if all products were retrieved successfully
    assert len(products) == 2
    assert products[0].name == "Product 1"
    assert products[0].price == 9.99
    assert products[1].name == "Product 2"
    assert products[1].price == 19.99


def test_update_product(test_db):
    # Add a test product to the database
    product = Product(name="Test Product", price=10.99, in_stock=True)
    test_db.add(product)
    test_db.commit()

    # Update the product in the database
    product_update = ProductUpdate(price=19.99)
    updated_product = update_product(test_db, "Test Product", product_update)

    # Check if the product was updated successfully
    assert updated_product.name == "Test Product"
    assert updated_product.price == 19.99
    assert updated_product.in_stock is True


def test_update_nonexistent_product_without_name(test_db):
    # Attempt to update a product that doesn't exist
    product_update = ProductUpdate(price=19.99)
    with pytest.raises(ValidationError) as exc_info:
        update_product(test_db, "Nonexistent Product", product_update)
        assert exc_info.value.errors() == [{'loc': ('name',), 'msg': 'Field required', 'type': 'missing'}]


def test_update_nonexistent_product_with_name(test_db):
    # Attempt to update a product that doesn't exist
    product_update = ProductUpdate(name="Nonexistent Product", price=19.99)
    updated_product = update_product(test_db, "Nonexistent Product", product_update)

    # Check if the function returns a new product
    assert updated_product is not None
    assert updated_product.name == "Nonexistent Product"
    assert updated_product.price == 19.99


def test_delete_product(test_db):
    # Add a test product to the database
    product = Product(name="Test Product", price=10.99)
    test_db.add(product)
    test_db.commit()

    # Delete the product from the database
    deleted_product = delete_product(test_db, "Test Product")

    # Check if the product was deleted successfully
    assert deleted_product is not None
    assert deleted_product.name == "Test Product"
    assert deleted_product.price == 10.99


def test_delete_nonexistent_product(test_db):
    # Attempt to delete a product that doesn't exist
    deleted_product = delete_product(test_db, "Nonexistent Product")

    # Check if the function returns None
    assert deleted_product is None
