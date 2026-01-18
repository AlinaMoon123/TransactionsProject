from fastapi import APIRouter, Depends
from src.transactions_project.services.transactionTypes import create_type
from src.transactions_project.db.base import get_db
from src.transactions_project.schemas.transactionTypeSchemas import CreateType
from sqlalchemy.ext.asyncio import AsyncSession


router = APIRouter(tags=["Тип транзакций"])

@router.post("/transactionType")
async def create_transactionType(transactionType: CreateType, db: AsyncSession = Depends(get_db)):
    db_type = await create_type(transactionType, db)
    return db_type
