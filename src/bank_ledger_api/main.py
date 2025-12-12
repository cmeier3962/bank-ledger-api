from fastapi import FastAPI, HTTPException
from bank_ledger.ledger import Ledger
from bank_ledger.errors import LedgerError
from .schemas import AccountCreate, AccountResponse, DepositRequest, WithdrawRequest

app = FastAPI(title="Bank Ledger API", version="0.1.0")

ledger = Ledger()


@app.post("/accounts", response_model=AccountResponse)
def create_account(data: AccountCreate):
    try:
        ledger.create_account(data.name)
        return {"name": data.name, "balance": ledger.get_balance(data.name)}
    except LedgerError as e:
        raise HTTPException(status_code=400, detail=str(e))
    

@app.get("/accounts/{name}/balance", response_model=AccountResponse)
def get_balance(name: str):
    try:
        balance = ledger.get_balance(name)
        return {"name": name, "balance": balance}
    except LedgerError as e:
        raise HTTPException(status_code=404, detail=str(e))


@app.post("/accounts/{name}/deposit", response_model=AccountResponse)
def deposit(name: str, data: DepositRequest):
    try:
        new_balance = ledger.deposit(name, data.amount)
        return {"name": name, "balance": new_balance}
    except LedgerError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/accounts/{name}/withdraw", response_model=AccountResponse)
def withdraw(name: str, data: WithdrawRequest):
    try:
        new_balance = ledger.withdraw(name, data.amount)
        return {"name": name, "balance": new_balance}
    except LedgerError as e:
        raise HTTPException(status_code=400, detail=str(e))