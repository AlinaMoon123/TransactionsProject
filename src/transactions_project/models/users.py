from datetime import datetime, timezone
from sqlalchemy import *
from src.transactions_project.db.base import Base

class Users(Base):
    __tablename__="users"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    password = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    update_at = Column(DateTime, nullable=True)

