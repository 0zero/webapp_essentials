from contextlib import asynccontextmanager
from logging import INFO, basicConfig, getLogger
from typing import AsyncGenerator

from fastapi import FastAPI

from src.database.database_setup import create_db_and_tables
from src.routers import product

logger = getLogger(__name__)
basicConfig(level=INFO)


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    """
    A generator function that handles the lifespan events of the FastAPI application.

    Args:
        app (FastAPI): The FastAPI application instance.

    Yields:
        None: This function is a generator and yields None.

    """
    logger.info("Starting up...")
    create_db_and_tables()
    yield
    logger.info("Shutting down...")
    logger.info("Finished shutting down.")


def get_app() -> FastAPI:
    """
    Returns a FastAPI application instance with the title "FastAPI Products".
    """
    app = FastAPI(title="FastAPI Products", lifespan=lifespan)
    app.include_router(product.router)
    return app


app = get_app()
