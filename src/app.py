"""Module responsible for the FastAPI application and its routes."""

from contextlib import asynccontextmanager
from fastapi import FastAPI
from loguru import logger

from src.db.connection import get_poem_by_id, init_db



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


@app.get("/")
def hello_world():
    return {"message": "Hello, World!"}


@app.get('/literary_works/{id}')
async def get_poem(id: int):
    return await get_poem_by_id(int(id))
