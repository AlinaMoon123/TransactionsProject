from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class CreateType(BaseModel):
    name: str
    description: Optional[str] = None