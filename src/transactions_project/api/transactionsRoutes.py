from fastapi import APIRouter, Depends
from src.transactions_project.services.transactions import *
from src.transactions_project.db.base import get_db
from sqlalchemy.ext.asyncio import AsyncSession

from src.transactions_project.schemas.usersSchemas import User
from src.transactions_project.auth.jwt import get_current_user


router = APIRouter(prefix='/transactions', tags=["Транзакции"])


@router.post("")
async def endpoint(transaction: CreateTransaction, current_user: User = Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    db_transaction = await create_transaction(transaction, current_user.id, db)
    return db_transaction


@router.delete("")
async def endpoint(transaction_id: int , current_user: User = Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    deleted_transaction_id = await transaction_delete(transaction_id, current_user.id, db)
    return {"id": deleted_transaction_id}


@router.get("")
async def endpoint(current_user: User = Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    transactions = await get_all_transactions(current_user.id, db)
    return transactions

# TODO перевести весь код в async/await 
