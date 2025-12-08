from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from config import settings

import logging
logger = logging.getLogger(__name__)

# Create async engine
engine = create_async_engine(
    settings.DATABASE_URL,
    echo=True,
    future=True
)

# Create async session
async_session = sessionmaker(
    engine, 
    class_=AsyncSession, 
    expire_on_commit=False, 
    autoflush=False
)

# # Create Base class
Base = declarative_base()


async def get_db() -> AsyncSession:
    """
    Dependency function that yields an async SQLAlchemy session.
    Correctly uses 'async with' for session management.
    """
    async with async_session() as session:
        try:
            yield session
        except Exception as e:
            logger.error(f"Session rollback due to exception: {e}", exc_info=True)
            await session.rollback()
            raise