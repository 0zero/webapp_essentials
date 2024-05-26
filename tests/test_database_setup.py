"""
This module contains tests for the database_setup module.
"""

import sqlalchemy
from sqlmodel import Session, SQLModel

from src.database.database_setup import get_session


def test_create_db_and_tables(test_db: Session):
    test_engine = test_db.get_bind()

    SQLModel.metadata.create_all(test_engine)

    inspector = sqlalchemy.inspect(test_engine)
    assert inspector.has_table("product")


def test_get_session():
    session_generator = get_session()

    session = next(session_generator)

    try:
        assert isinstance(session, Session)
    finally:
        session_generator.close()
