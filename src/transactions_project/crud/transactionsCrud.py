from src.transactions_project.models.transactionTypes import TransactionTypes
from src.transactions_project.schemas.transactionsSchemas import *
from src.transactions_project.models.transactions import Transactions
from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession

async def create(transaction: CreateTransaction, cur_user_id: int, db: AsyncSession):
    db_transaction = Transactions(user_id=cur_user_id, type_id=transaction.type_id, amount = transaction.amount, category = transaction.category, status = transaction.status)
    db.add(db_transaction)
    await db.commit()
    await db.refresh(db_transaction)
    return db_transaction


async def deleteTransaction(transaction_id: int, db: AsyncSession):
    stmt = delete(Transactions).where(Transactions.id == transaction_id)
    await db.execute(stmt)
    await db.commit()
    return transaction_id


async def findTransactionById(transaction_id: int, db: AsyncSession):
    stmt = select(Transactions).where(Transactions.id==transaction_id)
    res = await db.execute(stmt)
    return res.scalars().first()
    


async def findTransactions(user_id: int, db: AsyncSession):
    stmt = select(Transactions).where(Transactions.user_id == user_id)
    result = await db.execute(stmt)
    trans = result.scalars().all()
    print(trans)
    return trans