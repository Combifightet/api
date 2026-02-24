"""Module responsible for running the webserver instance."""


import os
from time import sleep
import uvicorn
from loguru import logger

from src.app import app
from src.config import settings



if __name__ == '__main__':
    duration: float = 15
    logger.debug(f'Started main function, sleeping for {duration} sconds')
    sleep(duration)
    print(f'HOST = {os.getenv('HOST', 'localhost (didn\'t find it)')}')
    logger.debug('sleeping finished, starting uvicorn server')

    uvicorn.run(
        app,
        host=settings.HOST,
        port=settings.PORT,
    )

    logger.debug('uvicorn server terminated')
