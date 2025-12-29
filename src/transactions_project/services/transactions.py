from fastapi import HTTPException
from sqlalchemy.orm import Session
from src.transactions_project.schemas.transactionsSchemas import CreateTransaction
from src.transactions_project.crud.transactionsCrud import *


def create_transaction(transaction: CreateTransaction, db: Session):
    db_transaction = create(transaction, db)
    return db_transaction

def transaction_delete(transaction_id: int, db: Session):
    db_transaction = findTransactionById(transaction_id, db)
    if not db_transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")
    deleted_transaction_id = deleteTransaction(transaction_id, db)
    return deleted_transaction_id