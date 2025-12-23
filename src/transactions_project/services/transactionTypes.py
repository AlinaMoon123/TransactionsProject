from fastapi import HTTPException
from sqlalchemy.orm import Session
from src.transactions_project.schemas.transactionTypeSchemas import *
from src.transactions_project.crud.transactionTypesCrud import *

def create_type(type: CreateType, db: Session):
    db_type = create(type, db)
    return db_type
