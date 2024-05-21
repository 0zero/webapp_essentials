from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from src.database.crud_operations import (
    delete_product,
    get_all_products,
    get_product,
    post_product,
    update_product,
)
from src.database.database_setup import get_session
from src.database.product import Product, ProductCreate, ProductUpdate

router = APIRouter(
    tags=["products"], responses={404: {"description": "No products found, sorry!"}}
)


@router.post("/products/", response_model=Product, status_code=201)
def create(product: ProductCreate, session: Session = Depends(get_session)) -> Product:
    """
    Create a new product.

    Args:
        product (ProductBase): The product data to create.
        session (Session, optional): The database session. Defaults to Depends(get_session).

    Returns:
        Product: The created product.
    """
    new_product = Product.model_validate(product)
    return post_product(session, new_product)


@router.get("/products/{product_name}", response_model=Product, status_code=200)
def get_by_name(product_name: str, session: Session = Depends(get_session)) -> Product:
    """
    Retrieve a product by its name.

    Args:
        product_name (str): The name of the product to retrieve.
        session (Session, optional): The database session. Defaults to Depends(get_session).

    Returns:
        Product: The retrieved product.

    Raises:
        HTTPException: If the product is not found.
    """
    product = get_product(session, product_name)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@router.get("/products/", response_model=list[Product], status_code=200)
def get_many(session: Session = Depends(get_session)) -> list[Product]:
    """
    Retrieve all products from the database.

    Parameters:
    - session: The database session to use (default: Depends(get_session))

    Returns:
    - A list of Product objects representing all the products in the database.
    """
    return get_all_products(session)


@router.put("/products/{product_name}", response_model=Product, status_code=201)
def update_by_name(
    product_name: str,
    product: ProductUpdate,
    session: Session = Depends(get_session),
) -> Product:
    """
    Update a product by its name.

    Args:
        product_name (str): The name of the product to be updated.
        product (ProductUpdate): The updated product data.
        session (Session, optional): The database session. Defaults to Depends(get_session).

    Returns:
        Product: The updated product.

    Raises:
        HTTPException: If the product is not found.
    """

    updated_product = update_product(session, product_name, product)
    if not updated_product:
        raise HTTPException(status_code=404, detail="Product not found")
    return updated_product


@router.delete("/products/{product_name}", response_model=Product, status_code=200)
def delete_by_name(product_name: str, session: Session = Depends(get_session)) -> Product:
    """
    Deletes a product from the database by its name.

    Args:
        product_name (str): The name of the product to be deleted.
        session (Session, optional): The database session. Defaults to Depends(get_session).

    Returns:
        Product: The deleted product.

    Raises:
        HTTPException: If the product is not found in the database.
    """
    deleted_product = delete_product(session, product_name)
    if not deleted_product:
        raise HTTPException(status_code=404, detail="Product not found")
    return deleted_product
