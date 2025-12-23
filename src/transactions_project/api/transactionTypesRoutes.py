from fastapi import APIRouter, Depends
from src.transactions_project.services.transactionTypes import *
from src.transactions_project.db.base import get_db
from src.transactions_project.schemas.transactionTypeSchemas import CreateType
from sqlalchemy.orm import Session


router = APIRouter()

@router.post("/transactionType")
def create_transactionType(transactionType: CreateType, db: Session = Depends(get_db)):
    db_type = create_type(transactionType, db)
    return db_type
