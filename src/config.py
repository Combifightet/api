""" Config vor global environment variables."""


from pathlib import Path
from pydantic_settings import BaseSettings
from pydantic_settings.main import SettingsConfigDict



class Settings(BaseSettings):
    """ Utility class that holds all global settings variables"""
    DATABASE_URL: str = 'postgresql+asyncpg://user:password@127.0.0.1:5432/dbname'
    HOST: str = 'localhost'
    PORT: int = 8000

    model_config = SettingsConfigDict(
        env_file='.env' if Path('.env').exists() else None,
        extra='ignore'
    )

settings: Settings = Settings()


if __name__ == '__main__':
    print(settings.model_dump())
