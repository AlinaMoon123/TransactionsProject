from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class CreateTransaction(BaseModel):
    type_id: int
    amount: int
    category: str
    status: str

class Transaction(CreateTransaction):
    id: int
    creater_at: datetime

    class Config:
        from_attributes = True
