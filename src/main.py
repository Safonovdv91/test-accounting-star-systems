from fastapi import FastAPI
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

from redis import asyncio as aioredis
from src.auth.base_config import fastapi_users, current_user, auth_backend
from src.auth.schemas import UserRead, UserCreate

from src.operation.router import router as router_operation
from src.tasks.router import router as router_tasks


app = FastAPI()
# добавление

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(
    router_operation
)
app.include_router(router_tasks)


@app.on_event("startup")
async def startup_event():
    redis = aioredis.from_url("redis://localhost")
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
