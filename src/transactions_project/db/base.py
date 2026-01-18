from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from src.transactions_project.core.config import DATABASE_URL

engine = create_async_engine(url=DATABASE_URL)

SessionLocal = async_sessionmaker(class_=AsyncSession, bind=engine, expire_on_commit=False)

Base = declarative_base()

async def get_db():
    async with SessionLocal() as db:
        try:
            yield db
        except:
            await db.rollback()
        finally:
            await db.close()

