import asyncio
from typing import AsyncGenerator

import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient

from database import get_async_session
from src import metadata

from src.config import (DB_HOST_TEST, DB_NAME_TEST, DB_PASS_TEST, DB_PORT_TEST, DB_USER_TEST)
from src.main import app

# database
DATABASE_URL_TEST = f"postgresql+asyncpg://{DB_USER_TEST}:{DB_PASS_TEST}@{DB_HOST_TEST}:{DB_PORT_TEST}/{DB_NAME_TEST}"
Base = declarative_base()


engine_test = create_async_engine(DATABASE_URL_TEST)
async_session_maker = sessionmaker(engine_test, class_=AsyncSession, expire_on_commit=False)
metadata.bind = engine_test


# Переписывание зависимость сесии, чтобы подключалось к другой бд
async def override_get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session

# замена сессии на тестовую
app.dependency_overrides[get_async_session()] = override_get_async_session()


# Создаем начальную БД(таблицы) используя фикстуры
@pytest.fixture(autouse=True, scope='session')
async def prepare_database():
    # Создаем таблицы
    async with engine_test.begin() as conn:
        await conn.run_sync(metadata.create_all)
    yield   # Отдаем доступа для работы с ними
    # Уничтожаем созданные таблицы
    async with engine_test.begin as conn:
        await conn.run_sync(metadata.drop_all)


# SETUP
# Из документации -> крайне желательно создавать эвент луп
@pytest.fixture(scope='session')
def event_loop(request):
    """Create an instance of the default event loop for each test case."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()

client = TestClient(app)

@pytest.fixture(scope='session')
async def ac() -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac
