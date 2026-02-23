""" This module handles the actual database connection."""



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
        statement = text("SELECT * FROM poems WHERE poems.id = :id")

        result = await session.exec(statement, params={'id': 4})

        print(result)
        print(result.all())

async def get_poem_by_id(id: int):
    async with AsyncSession(bind=async_engine) as session:
        statement = text("SELECT * FROM poems WHERE poems.id = :id")

        result = await session.exec(statement, params={'id': 4})

        poems = result.all()
        if len(poems) == 0:
            return None
        else:
            return poems[0]
