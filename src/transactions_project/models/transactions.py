from datetime import datetime, timezone
from sqlalchemy import Column, DateTime, ForeignKey, Integer, Numeric, String
from src.transactions_project.db.base import Base

class Transactions(Base):
    __tablename__="transactions"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    type_id = Column(Integer, ForeignKey("transactiontypes.id"))
    amount = Column(Numeric, nullable=False)
    category = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    status = Column(String, nullable=False)
    
