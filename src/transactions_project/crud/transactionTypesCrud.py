from src.transactions_project.schemas.transactionTypeSchemas import *
from sqlalchemy.orm import Session
from src.transactions_project.models.transactionTypes import TransactionTypes

def create(type: CreateType, db: Session):
    db_type = TransactionTypes(name = type.name, description = type.description)
    db.add(db_type)
    db.commit()
    db.refresh(db_type)
    return db_type