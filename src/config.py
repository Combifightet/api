""" Config vor global environment variables."""

from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """ Utility class that holds all global settings variables"""
    DATABASE_URL: str = 'postgresql+asyncpg://public_api:public_api_password@192.168.2.202@2566/cbf_db'
    HOST: str = 'localhost'
    PORT: int = 8000

    model_config = SettingsConfigDict(
        env_file='.env' if Path('.env').exists() else None,
        extra='ignore'
    )

settings: Settings = Settings()


if __name__ == '__main__':
    print(settings.model_dump())
