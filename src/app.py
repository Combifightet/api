"""Module responsible for the FastAPI application and its routes."""

from fastapi import FastAPI
from contextlib import asynccontextmanager
from loguru import logger



@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting server . . .")

    yield
    logger.info("Shutting server down . . .")


app = FastAPI(
    title='CBF API',
    version='0.1.0',
    description='A simple FastAPI for my personal projects / PostgreSQL database',
    lifespan=lifespan
)


@app.get("/")
def hello_world():
    return {"message": "Hello, World!"}

@app.get('/ping')
def get_ping():
    return 'pong'