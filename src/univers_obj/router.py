from fastapi import APIRouter

router = APIRouter(
    prefix='/universe_objects',
    tags=['Universe_Objects']
)

@router.get('/')
async def get_obj():
    return


