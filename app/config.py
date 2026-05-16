from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    app_name: str = "FileMaster AI Bot"
    environment: str = Field(default="development")
    telegram_bot_token: str = Field(default="")
    telegram_admin_ids: str = Field(default="")

    postgres_dsn: str = Field(default="postgresql+asyncpg://postgres:postgres@db:5432/filemaster")
    redis_url: str = Field(default="redis://redis:6379/0")

    max_file_size_mb_free: int = 25
    max_file_size_mb_premium: int = 2048
    storage_retention_hours: int = 24


settings = Settings()
