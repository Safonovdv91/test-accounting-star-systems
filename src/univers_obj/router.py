from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from src.univers_obj.models import celestials
from src.univers_obj.schemas import UniverseObjectCreate

router = APIRouter(
    prefix='/universe_objects',
    tags=['Universe_Objects']
)


@router.post('/')
async def add_specific_operation(new_universe_object: UniverseObjectCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(celestials).values(**new_universe_object.dict())
    await session.execute(stmt)
    await session.commit()
    return {
        'status': 200,
        'data': {
            'data': f'{new_universe_object.dict()}',
            'detail': 'Adding success'
        },
        'details': 'update success'
    }


@router.get('/')
async def get_specific_operation(session: AsyncSession = Depends(get_async_session)):
    # query - запрос на выборку
    # stmt - запрос на удаление, вставку
    try:
        query = select(celestials)
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


@router.get('/hello')
async def get_hello(session: AsyncSession = Depends(get_async_session)):
    # query - запрос на выборку
    # stmt - запрос на удаление, вставку
    try:
        return {
            'status': '200',
            'data': ['hello', 'hello2'],
            'detail': None
        }
    except Exception:
        raise HTTPException(status_code=500, detail={
            'satus': 'error',
            'data': None,
            'detail': None
        })
