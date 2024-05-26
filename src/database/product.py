from sqlmodel import Field, SQLModel


class ProductBase(SQLModel):
    """
    Represents a base product.

    Attributes:
        name (str): The name of the product.
        description (str | None): The description of the product (optional).
        price (float | None): The price of the product (optional).
        in_stock (bool): Indicates if the product is in stock.
    """
    name: str = Field(index=True)
    description: str | None = Field(default=None)
    price: float | None = Field(default=None)
    in_stock: bool = Field(default=False, index=True)


class Product(ProductBase, table=True):
    """
    Represents a product in the database.

    Attributes:
        id (int | None): The ID of the product. Defaults to None. 
                         Primary key in database.
    """
    id: int | None = Field(default=None, primary_key=True)


class ProductCreate(ProductBase):
    """
    Represents a product creation instance.

    This class inherits from the `ProductBase` class and is used to define the attributes
    required to create a new product.
    """
    pass


class ProductUpdate(SQLModel):
    """
    Represents an update for a product.

    Attributes:
        name (str | None): The updated name of the product.
        description (str | None): The updated description of the product.
        price (float | None): The updated price of the product.
        in_stock (bool | None): The updated stock availability of the product.
    """
    name: str | None = None
    description: str | None = None
    price: float | None = None
    in_stock: bool | None = None
