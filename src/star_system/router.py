from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from src.star_system.models import star_system
from src.star_system.schemas import StarSystemCreate

router = APIRouter(
    prefix='/star_system',
    tags=['Stars System']
)

@router.post('/')
async def add_specific_operation(new_star_system: StarSystemCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(star_system).values(**new_star_system.dict())
    await session.execute(stmt)
    await session.commit()
    return {
        'status': 200,
        'data': {
            'data': f'{new_star_system.dict()}',
            'detail': 'Adding success'
        },
        'details': 'update success'
    }

@router.get('/')
async def get_specific_operation(systemId: int, session: AsyncSession = Depends(get_async_session)):
    # query - запрос на выборку
    # stmt - запрос на удаление, вставку
    try:
        query = select(star_system)\
            .where(star_system.c.systemId == systemId)
        result = await session.execute(query)
        return {
            'status': '200',
            'data': result.all(),
            'detail': None
        }
    except Exception:
        raise HTTPException(status_code=500, detail={
            'satus': 'error',
            'data': None,
            'detail': None
        })



