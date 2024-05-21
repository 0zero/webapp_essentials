from sqlmodel import Field, SQLModel


class ProductBase(SQLModel):
    name: str = Field(index=True)
    weight: float | None = Field(default=None)
    default_quantity: int = Field(default=1)


class Product(ProductBase, table=True):
    id: int | None = Field(default=None, primary_key=True)


class ProductCreate(ProductBase):
    pass


class ProductUpdate(SQLModel):
    name: str | None = None
    weight: float | None = None
    default_quantity: int | None = None
