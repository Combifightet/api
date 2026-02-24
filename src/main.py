"""Module responsible for running the webserver instance."""


from time import sleep
import uvicorn
from loguru import logger

from src.app import app
from src.config import settings



if __name__ == '__main__':
    duration: float = 15
    logger.debug('Started main function')
    sleep(duration)

    logger.info(f'DATABASE_URL (pydantic)  = {settings.DATABASE_URL}')
    logger.info(f'HOST (pydantic)  = {settings.HOST}')
    logger.info(f'PORT (pydantic)  = {settings.PORT}')

    logger.debug('Starting uvicorn server')

    uvicorn.run(
        app,
        host=settings.HOST,
        port=settings.PORT,
    )

    logger.debug('Terminated uvicorn server')
