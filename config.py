from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


class Settings(BaseSettings):
    # Database settings
    DATABASE_URL: str
    MEDIA_ROOT: Path = BASE_DIR / "uploads"      # physical folder
    MEDIA_URL: str = "/uploads"
    model_config = SettingsConfigDict(env_file=".env", case_sensitive=True)

settings = Settings()