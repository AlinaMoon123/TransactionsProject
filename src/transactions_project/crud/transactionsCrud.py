from src.transactions_project.models.transactionTypes import TransactionTypes
from src.transactions_project.schemas.transactionsSchemas import *
from sqlalchemy.orm import Session
from src.transactions_project.models.transactions import Transactions
from sqlalchemy import delete

def create(transaction: CreateTransaction, db: Session):
    db_transaction = Transactions(user_id=transaction.user_id, type_id=transaction.type_id, amount = transaction.amount, category = transaction.category, status = transaction.status)
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction

def deleteTransaction(transaction_id: int, db: Session):
    stmt = delete(Transactions).where(Transactions.id == transaction_id)
    db.execute(stmt)
    db.commit()
    return transaction_id

def findTransactionById(transaction_id: int, db: Session):
    return db.query(Transactions).filter(Transactions.id==transaction_id).first()