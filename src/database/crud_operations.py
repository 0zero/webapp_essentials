from sqlmodel import Session, select

from src.database.database_setup import engine
from src.database.product import Product, ProductUpdate


def post_product(session: Session, product: Product) -> Product:
    """
    Adds a new product to the database.

    Args:
        product (Product): The product object to be added.

    Returns:
        Product: The added product object.

    """
    session.add(product)
    session.commit()
    session.refresh(product)
    return product


def get_product(session: Session, product_name: str) -> Product | None:
    """
    Retrieve a product from the database by its name.

    Args:
        product_name (str): The name of the product to retrieve.

    Returns:
        Product: The retrieved product.

    """
    query = select(Product).where(Product.name == product_name)
    return session.exec(query).first()


def get_all_products(session: Session) -> list[Product]:
    """
    Retrieve all products from the database.

    Returns:
        list[Product]: A list of all products in the database.

    """
    return session.exec(select(Product)).all()  # type: ignore


def update_product(session: Session, product_name: str, product_update: ProductUpdate) -> Product:
    """
    Update a product in the database with the given product name and data.

    Args:
        product_name (str): The name of the product to be updated.
        product_update(ProductUpdate): The updated data for the product.

    Returns:
        Product: The updated product object.

    Raises:
        None

    """
    product_data = product_update.model_dump(exclude_unset=True)

    product = session.exec(select(Product).where(Product.name == product_name)).first()
    if not product:
        return post_product(session, Product.model_validate(product_data))
    for key, value in product_data.items():
        setattr(product, key, value)

    session.add(product)
    session.commit()
    session.refresh(product)
    return product


def delete_product(session: Session, product_name: str) -> Product | None:
    """
    Deletes a product from the database.

    Args:
        product_name (str): The name of the product to delete.

    Returns:
        Product: The deleted product, or None if the product doesn't exist.
    """
    with Session(engine) as session:
        product = session.exec(select(Product).where(Product.name == product_name)).first()
        if not product:
            return None
        session.delete(product)
        session.commit()
    return product
