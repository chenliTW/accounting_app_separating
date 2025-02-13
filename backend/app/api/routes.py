from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import SessionLocal

router = APIRouter()

# 資料庫 session 依賴
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/accounts", response_model=list[schemas.account.Account])
def read_accounts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    accounts = crud.account.get_accounts(db, skip=skip, limit=limit)
    return accounts

@router.post("/accounts", response_model=schemas.account.Account)
def create_account(account: schemas.account.AccountCreate, db: Session = Depends(get_db)):
    return crud.account.create_account(db, account)
