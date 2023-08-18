from fastapi import APIRouter, Depends, HTTPException
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


@router.patch('/update_type')
async def patch_operation_id_type(operation_id: int, new_type: str, session: AsyncSession = Depends(get_async_session)):
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

test = [{
  "id": 0,
  "quantity": "21",
  "figi": "sber",
  "instrument_type": "bond",
  "date": "2023-08-18T09:15:52.705",
  "type": "Buy"
},{
  "id": 1,
  "quantity": "10",
  "figi": "tink",
  "instrument_type": "bond",
  "date": "2023-08-18T09:06:54.705",
  "type": "Sell"
},{
  "id": 2,
  "quantity": "17",
  "figi": "luk",
  "instrument_type": "bond",
  "date": "2023-08-17T08:14:50.705",
  "type": "Sell"
},{
  "id": 3,
  "quantity": "8",
  "figi": "sber",
  "instrument_type": "bond",
  "date": "2023-08-18T10:45:21.705",
  "type": "Buy"
},{
  "id": 4,
  "quantity": "15",
  "figi": "tink",
  "instrument_type": "bond",
  "date": "2023-08-17T11:32:40.705",
  "type": "Sell"
}, {
  "id": 5,
  "quantity": "12",
  "figi": "luk",
  "instrument_type": "bond",
  "date": "2023-08-18T11:20:15.705",
  "type": "Buy"
}, {
  "id": 6,
  "quantity": "19",
  "figi": "sber",
  "instrument_type": "bond",
  "date": "2023-08-17T14:55:30.705",
  "type": "Sell"
}, {
  "id": 7,
  "quantity": "9",
  "figi": "tink",
  "instrument_type": "bond",
  "date": "2023-08-18T12:40:48.705",
  "type": "Buy"
}, {
  "id": 8,
  "quantity": "16",
  "figi": "luk",
  "instrument_type": "bond",
  "date": "2023-08-17T15:25:10.705",
  "type": "Sell"
}, {
  "id": 9,
  "quantity": "7",
  "figi": "sber",
  "instrument_type": "bond",
  "date": "2023-08-18T13:10:22.705",
  "type": "Buy"
}]
for each in test:
    print(each)

