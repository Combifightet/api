""" This module handles the actual database connection."""


from typing import Any
from loguru import logger
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio.engine import AsyncEngine
from sqlmodel import text
from sqlmodel.ext.asyncio.session import AsyncSession

from src.config import settings



async_engine: AsyncEngine = create_async_engine(
    url=settings.DATABASE_URL,
    echo=True
)



async def init_db():
    async with AsyncSession(bind=async_engine) as session:
        statement = text("SELECT * FROM literary_works WHERE literary_works.id = :id")

        result = await session.exec(statement, params={'id': 4})

        print(result)
        print(result.all())


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
