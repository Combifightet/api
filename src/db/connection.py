""" This module handles the actual database connection."""


from typing import Any
import asyncpg
from loguru import logger
from sqlalchemy.exc import ProgrammingError, SQLAlchemyError
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio.engine import AsyncEngine
from sqlalchemy.orm import sessionmaker
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import SQLModel, text

from src.config import settings


async_engine: AsyncEngine = create_async_engine(
    url=settings.DATABASE_URL,
    echo=True
)



async def init_db():
    ''' Initializes the database and tries to crate all tables defined in `src.db.models`'''
    try:
        async with async_engine.begin() as conn:
            from src.db.models import LiteraryWork
            await conn.run_sync(SQLModel.metadata.create_all)
    except (asyncpg.exceptions.InsufficientPrivilegeError, ProgrammingError, SQLAlchemyError) as e:
        logger.warning(e)



async def get_session() -> AsyncSession:
    async_session = sessionmaker(
        bind=async_engine,
        class_=AsyncSession,
        expire_on_commit=False
    )

    async with async_session() as session:
        yield session



async def get_poem_by_id(id: int):
    async with AsyncSession(bind=async_engine) as session:
        statement = text("SELECT * FROM literary_works WHERE literary_works.id = :id")

        result = await session.exec(statement, params={'id': id})

        works = result.all()
        if len(works) == 0:
            logger.warning(f'Couldn\'t find any poem with the id: {id} ')
            return None
        else:
            work = works[0]
            result: dict[str, Any]
            try:
                result = dict(work._mapping)
            except Exception:
                try:
                    result = dict(work)
                except Exception:
                    result = {
                        'value': str(work)
                    }

            logger.info(f'Returning poem no. {id} -> "{result.get('title', '')}"')
            return result
