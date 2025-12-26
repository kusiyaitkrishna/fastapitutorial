from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


class Settings(BaseSettings):
    # Database settings
    DATABASE_URL: str
    MEDIA_ROOT: Path = BASE_DIR / "uploads" # physical folder jaha hamro actual data save hunxa
    MEDIA_URL: str = "/uploads" # virtual path jaha bata hamro data access hunxa
    BASE_URL: str = "http://localhost:8000" 
    model_config = SettingsConfigDict(env_file=".env", case_sensitive=True)

settings = Settings()