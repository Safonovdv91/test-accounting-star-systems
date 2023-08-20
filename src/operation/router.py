import time

from src.auth.base_config import current_user

from fastapi import APIRouter, Depends, HTTPException
from fastapi_cache.decorator import cache
from sqlalchemy import select, insert, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from src.operation.models import operation
from src.operation.schemas import OperationCreate

router = APIRouter(
    prefix='/operations',
    tags=['operation']
)


@router.get('/')
async def get_specific_operation(operation_type: str, session: AsyncSession = Depends(get_async_session)):
    # query - запрос на выборку
    # stmt - запрос на удаление, вставку
    try:
        query = select(operation)\
            .where(operation.c.type == operation_type)
        # query = select(operation)
        result = await session.execute(query)
        lk = result.all()
        return {
            'status': '200',
            'data': lk[0],
            'detail': None
        }
    except Exception:
        raise HTTPException(status_code=500, detail={
            'satus': 'error',
            'data': None,
            'detail': None
        })


@router.patch('/update_type')
async def patch_operation_id_type(
        operation_id: int,
        new_type: str,
        session: AsyncSession = Depends(get_async_session)):
    try:
        query = select(operation).\
            where(operation.c.id == operation_id)
        result = await session.execute(query)
        if not result.all():
            return {
                'status': 'error',
                'data': None,
                'detail': f'Operation with id = {operation_id} is not exist'
            }

        stmt = (
            update(operation)
            .where(operation.c.id == operation_id)
            .values(instrument_type=new_type)
        )
        print(stmt)
        await session.execute(stmt)
        await session.commit()
        return {
            'status': 200,
            'data': {
                'operationd_id': operation_id,
                'instrument_type': new_type
            },
            'details': 'update success'
        }
    except Exception:
        raise HTTPException(status_code=500, detail={
            'satus': 'error',
            'data': None,
            'detail': None
        })


@router.delete('/')
async def delete_operation_id(operation_id: int, session: AsyncSession =Depends(get_async_session)):
    try:
        stmt = (
            delete(operation).
            where(operation.c.id == operation_id)
            .returning(operation.c.id, operation.c.figi)
        )
        await session.execute(stmt)
        await session.commit()

        return {
            'status': 200,
            'data': {
                'operationd_id': operation_id,
                'data': f'operation_id: {operation_id} Deleting success'
            },
            'details': 'update success'
        }
    except:
        raise HTTPException(status_code=500, detail={
            'satus': 'error',
            'data': None,
            'detail': None
        })


@router.post('/')
async def add_specific_operation(new_operation: OperationCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(operation).values(**new_operation.dict())
    await session.execute(stmt)
    await session.commit()
    return {
        'status': 200,
        'data': {
            'data': f'{new_operation.dict()}',
            'detail': 'Adding success'
        },
        'details': 'update success'
    }


@router.get('/long_operation')
@cache(expire=30)
def get_long_operation():
    time.sleep(3)
    return {"long operation thinking"}
