from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List

class Settings(BaseSettings):
    # Database settings
    DATABASE_URL: str
    model_config = SettingsConfigDict(env_file=".env", case_sensitive=True)

settings = Settings()