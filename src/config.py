from functools import lru_cache
from logging import INFO, basicConfig, getLogger

from pydantic import AnyUrl
from pydantic_settings import BaseSettings

log = getLogger(__name__)
basicConfig(level=INFO)


class Settings(BaseSettings):
    """
    Represents the settings for the web application.
    """

    environment: str = "dev"
    testing: bool = bool(0)
    database_url: AnyUrl = None  # type: ignore


@lru_cache()
def get_settings() -> BaseSettings:
    """
    Retrieves the configuration settings for the application.

    Returns:
        An instance of the BaseSettings class containing the configuration settings.
    """
    log.info("Loading config settings from the environment...")
    return Settings()
