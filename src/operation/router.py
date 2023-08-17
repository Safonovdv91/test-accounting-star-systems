from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
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
    query = select(operation).where(operation.c.type == operation_type)
    result = await session.execute(query)
    return result.all()

@router.post('/')
async def add_specific_operation(new_operation: OperationCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(operation).values(**new_operation.dict())
    await session.execute(stmt)
    await session.commit()
    return {'status': 'success'}
