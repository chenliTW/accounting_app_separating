from pydantic import BaseModel
from datetime import datetime

class AccountBase(BaseModel):
    description: str
    amount: float

class AccountCreate(AccountBase):
    pass

class Account(AccountBase):
    id: int
    timestamp: datetime

    class Config:
        orm_mode = True
