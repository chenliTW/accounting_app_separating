from sqlalchemy.orm import Session
from app.models.account import Account
from app.schemas.account import AccountCreate

def get_accounts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Account).offset(skip).limit(limit).all()

def create_account(db: Session, account: AccountCreate):
    db_account = Account(**account.dict())
    db.add(db_account)
    db.commit()
    db.refresh(db_account)
    return db_account
