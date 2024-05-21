from functools import lru_cache
from logging import INFO, basicConfig, getLogger

from pydantic import AnyUrl
from pydantic_settings import BaseSettings

log = getLogger(__name__)
basicConfig(level=INFO)


class Settings(BaseSettings):
    environment: str = "dev"
    testing: bool = bool(0)
    database_url: AnyUrl = None  # type: ignore


@lru_cache()
def get_settings() -> BaseSettings:
    log.info("Loading config settings from the environment...")
    return Settings()
