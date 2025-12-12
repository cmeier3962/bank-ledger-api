from fastapi import FastAPI, HTTPException
from bank_ledger.ledger import Ledger
from bank_ledger.account import Account
from bank_ledger.errors import LedgerError

from .schemas import (
    AccountCreate,
    AccountResponse,
    AmountRequest,
    BalanceResponse,
    TransactionResponse,
    TransferRequest,
    TransferResponse
)

app = FastAPI(title="Bank Ledger API", version="0.1.0")

ledger = Ledger()


@app.post("/accounts", response_model=AccountResponse)
def create_account(data: AccountCreate):
    try:
        acct = Account(id=data.id, name=data.name, balance=data.initial_balance)
        ledger.add_account(acct)
        return AccountResponse(id=acct.id, name=acct.name, balance=acct.balance)
    except LedgerError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/accounts/{account_id}/balance", response_model=BalanceResponse)
def get_balance(account_id: str):
    try:
        balance = ledger.balance(account_id)
        return BalanceResponse(id=account_id, balance=balance)
    except LedgerError as e:
        raise HTTPException(status_code=404, detail=str(e))


@app.post("/accounts/{account_id}/deposit", response_model=TransactionResponse)
def deposit(account_id: str, data: AmountRequest):
    try:
        tx = ledger.deposit(account_id, data.amount)

        return TransactionResponse(
            tx_id=tx.tx_id,
            account_id=tx.account_id,
            amount=float(tx.amount),
            timestamp=tx.timestamp
        )
    except LedgerError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/accounts/{account_id}/withdraw", response_model=TransactionResponse)
def withdraw(account_id: str, data: AmountRequest):
    try:
        tx = ledger.withdraw(account_id, data.amount)
        
        return TransactionResponse(
            tx_id=tx.tx_id,
            account_id=tx.account_id,
            amount=float(tx.amount),
            timestamp=tx.timestamp
        )
    except LedgerError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/transfer", response_model=TransferResponse)
def transfer(data: TransferRequest):
    try:
        wtx, dtx = ledger.transfer(data.from_id, data.to_id, data.amount)
        
        return TransferResponse(
            withdraw=TransactionResponse(
                tx_id=wtx.tx_id,
                account_id=wtx.account_id,
                amount=float(wtx.amount),
                timestamp=wtx.timestamp
                ),
            deposit=TransactionResponse(
                tx_id=dtx.tx_id,
                account_id=dtx.account_id,
                amount=float(dtx.amount),
                timestamp=dtx.timestamp
                )
        )
    except LedgerError as e:
        raise HTTPException(status_code=400, detail=str(e))