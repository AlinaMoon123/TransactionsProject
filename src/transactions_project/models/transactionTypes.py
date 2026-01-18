from datetime import datetime, timezone
from sqlalchemy import Column, DateTime, Integer, String 
from src.transactions_project.db.base import Base

class TransactionTypes(Base):
    __tablename__ = "transactiontypes"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))