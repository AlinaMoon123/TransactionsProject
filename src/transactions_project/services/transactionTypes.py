from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from src.transactions_project.schemas.transactionTypeSchemas import CreateType  
from src.transactions_project.crud.transactionTypesCrud import create

async def create_type(type: CreateType, db: AsyncSession):
    db_type = await create(type, db)
    return db_type
