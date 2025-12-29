from fastapi import APIRouter, Depends
from src.transactions_project.services.transactions import *
from src.transactions_project.db.base import get_db
from sqlalchemy.orm import Session


router = APIRouter()

@router.post('/transaction')
def register(transaction: CreateTransaction , db: Session = Depends(get_db)):
    db_transaction = create_transaction(transaction, db)
    return db_transaction

@router.delete('/transaction')
def delete_user(transaction_id: int , db: Session = Depends(get_db)):
    deleted_transaction_id = transaction_delete(transaction_id, db)
    return {"id": deleted_transaction_id}





