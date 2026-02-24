"""Module responsible for the FastAPI application and its routes."""

from starlette.responses import RedirectResponse


from contextlib import asynccontextmanager
from http import HTTPStatus
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from loguru import logger


from src.db.connection import init_db
from src.api.literary_works.routes import literary_works_router



@asynccontextmanager
async def lifespan(_app: FastAPI):
    """ Lifspan manager function"""
    logger.info("Starting server . . .")
    await init_db()

    yield
    logger.info("Shutting server down . . .")


app = FastAPI(
    title='CBF API',
    version='0.1.0',
    description='A simple FastAPI for my personal projects / PostgreSQL database',
    lifespan=lifespan
)


app.include_router(literary_works_router)


@app.get("/", include_in_schema=False)
def redirect_to_docs() -> RedirectResponse:
    ''' Redirects from the home to the swagger ui documentation.append()'''
    return RedirectResponse(url='/docs', status_code=HTTPStatus.SEE_OTHER)
