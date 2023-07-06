import uuid
from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    # Параметры для БД
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    DB_HOST: str
    DB_PORT: str
    # Параметры для проекта
    DEBUG: bool = False
    SECRET_KEY: str = str(uuid.uuid4())
    ROOT_PATH: str = ""

    @property
    def database_url(self) -> str:
        """Получить ссылку для подключения к DB."""
        return (
            "postgresql+asyncpg://"
            f"{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
            f"@{self.DB_HOST}:{self.DB_PORT}/{self.POSTGRES_DB}"
        )

    class Config:
        env_file = ".env.example"


@lru_cache()
def get_settings() -> Settings:
    return Settings()  # type: ignore


settings = get_settings()
