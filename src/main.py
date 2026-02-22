"""Module responsible for running the webserver instance."""


import uvicorn

from src.app import app
from src.config import settings



if __name__ == '__main__':
    uvicorn.run(
        app,
        host=settings.HOST,
        port=settings.PORT,
    )
