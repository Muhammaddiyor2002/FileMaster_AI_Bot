from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from app.config import settings

engine = create_async_engine(settings.postgres_dsn, future=True, pool_pre_ping=True)
SessionLocal = async_sessionmaker(engine, autoflush=False, autocommit=False, class_=AsyncSession)


async def get_db() -> AsyncSession:
    async with SessionLocal() as session:
        yield session
