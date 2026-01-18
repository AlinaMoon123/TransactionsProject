from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from src.transactions_project.schemas.transactionsSchemas import CreateTransaction
from src.transactions_project.crud.transactionsCrud import create, deleteTransaction, findTransactionById, findTransactions


async def create_transaction(transaction: CreateTransaction, user_id: int, db: AsyncSession):
    db_transaction = await create(transaction, user_id, db)
    return db_transaction


async def transaction_delete(transaction_id: int, user_id: int, db: AsyncSession):
    db_transaction = await findTransactionById(transaction_id, db)
    if not db_transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")
    if user_id != db_transaction.user_id:
        raise HTTPException(status_code=403, detail="Not allowed to delete")
    deleted_transaction_id = await deleteTransaction(transaction_id, db)
    return deleted_transaction_id


async def get_all_transactions(user_id: int, db: AsyncSession):
    transactions = await findTransactions(user_id, db)
    return transactions

