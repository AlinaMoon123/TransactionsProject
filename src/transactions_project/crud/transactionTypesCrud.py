from src.transactions_project.schemas.transactionTypeSchemas import *
from sqlalchemy.ext.asyncio import AsyncSession
from src.transactions_project.models.transactionTypes import TransactionTypes

async def create(type: CreateType, db: AsyncSession):
    db_type = TransactionTypes(name = type.name, description = type.description)
    db.add(db_type)
    await db.commit()
    await db.refresh(db_type)
    return db_type