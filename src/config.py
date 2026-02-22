from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """ Utility class that holds all global settings variables"""
    DATABASE_URL: str = 'postgresql+asyncpg://postgres:password@localhost:5432/postgres'
    HOST: str = 'localhost'
    PORT: int = 8000

    model_config = SettingsConfigDict(
        env_file = '.env',
        extra='ignore'
    )

settings: Settings = Settings()


if __name__ == '__main__':
    print(settings.model_dump())
