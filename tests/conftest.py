"""
This file contains the fixtures for the tests.
"""

import os
from contextlib import contextmanager
from typing import Generator

import pytest
from fastapi.testclient import TestClient
from sqlmodel import Session, SQLModel, create_engine

from src.config import Settings, get_settings
from src.database.database_setup import get_session
from src.main import get_app


def get_settings_override() -> Settings:
    """
    Override settings for test environment.
    """
    return Settings(testing=1, database_url=os.environ.get("DATABASE_TEST_URL"))


@contextmanager
def create_test_db() -> Generator[Session, None, None]:
    """
    Context manager for creating a test database session.
    """
    test_settings = get_settings()
    test_engine = create_engine(
        str(test_settings.database_url)
    )  # Ensure this is the test database URL
    session_local = Session(test_engine)

    SQLModel.metadata.create_all(test_engine)

    connection = test_engine.connect()
    transaction = connection.begin()
    test_session = session_local

    try:
        yield test_session
    finally:
        transaction.rollback()
        test_session.close()
        connection.close()
        SQLModel.metadata.drop_all(test_engine)


@pytest.fixture(scope="module")
def test_app() -> Generator[TestClient, None, None]:
    """
    Fixture for a test application without a database.
    """
    app = get_app()
    app.dependency_overrides[get_settings] = get_settings_override

    with TestClient(app) as test_client:
        yield test_client


@pytest.fixture(scope="function")
def test_db() -> Generator[Session, None, None]:
    """
    Fixture for a test database session.
    """
    with create_test_db() as test_session:
        yield test_session


def get_test_db(test_db: Session) -> Generator[Session, None, None]:
    """
    Dependency override function for providing the test database session.
    """
    try:
        yield test_db
    finally:
        pass


@pytest.fixture(scope="function")
def test_app_with_db(test_db: Session) -> Generator[TestClient, None, None]:
    """
    Fixture for a test application with a database.
    """
    app = get_app()
    app.dependency_overrides[get_settings] = get_settings_override
    app.dependency_overrides[get_session] = lambda: get_test_db(test_db)

    with TestClient(app) as test_client:
        yield test_client
