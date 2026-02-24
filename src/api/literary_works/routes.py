''' Module containing all routes for the literary works api.'''

from http import HTTPStatus
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession


from src.db.connection import get_session



literary_works_router = APIRouter(
    prefix='/literary_works'
)


@literary_works_router.get('/{id}', status_code=HTTPStatus.OK)
async def get_work(
    id: int,
    session: AsyncSession = Depends(get_session)
):
    # TODO: only so I can still debug
    return await get_poem_by_id(int(id))
    pass


@literary_works_router.post('/', status_code=HTTPStatus.CREATED)
async def add_work(
    session: AsyncSession = Depends(get_session)
):
    pass


@literary_works_router.put('/{id}', status_code=HTTPStatus.OK)
async def update_work(
    id: int,
    session: AsyncSession = Depends(get_session)
):
    pass


@literary_works_router.delete('/{id}', status_code=HTTPStatus.NO_CONTENT)
async def remove_work(
    id: int,
    session: AsyncSession = Depends(get_session)
):
    pass