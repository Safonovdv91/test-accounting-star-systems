from sqlalchemy import insert, select

from src.auth.models import role
from tests.conflest import client, async_session_maker


async def test_add_role():
    async with async_session_maker() as session:
        stmt = insert(role).values(id=4, name="admin", permissions=None)
        await session.execute(stmt)
        await session.commit()

        query = select(role)
        result = await session.execute(query)
        print(result.all())

# def test_register():
#     client.post("/auth/register", json={
#         "email": "Tester1@mail.ru",
#         "password": "string",
#         "is_active": True,
#         "is_superuser": False,
#         "is_verified": False,
#         "username": "string",
#         "role_id": 0
#     })
