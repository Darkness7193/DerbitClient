from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.pool import NullPool

from src.config import CONFIG
from src.db.models import Base, TickerData


ASYNC_DB_URL = f'postgresql+asyncpg://{CONFIG.POSTGRES_USER}:{CONFIG.POSTGRES_PASSWORD}@db/{CONFIG.POSTGRES_DB}'
SYNC_DB_URL =  f'postgresql+psycopg://{CONFIG.POSTGRES_USER}:{CONFIG.POSTGRES_PASSWORD}@db/{CONFIG.POSTGRES_DB}'

asyncEngine = create_async_engine(
    url=ASYNC_DB_URL,
    echo=True,
    poolclass=NullPool
)

syncEngine = create_engine(
    url=SYNC_DB_URL,
    echo=True
)

AsyncSession = async_sessionmaker(
    asyncEngine,
    expire_on_commit=False
)

SyncSession = sessionmaker(
    bind=syncEngine,
    expire_on_commit=False,
)

async def init_db():
    async with asyncEngine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)