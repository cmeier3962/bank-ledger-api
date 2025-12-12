from fastapi import FastAPI, HTTPException
from bank_ledger import Ledger, Account, AccountNotFoundError, InvalidAmountError
from .schemas import AccountCreate, AccountResponse
from typing import Any

app = FastAPI(title="Bank Ledger API", version="0.1.0")

# For now, a single in-memory Ledger instance.
# Later we can swap this out for a DB or something more advanced.
ledger = Ledger()


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/accounts", response_model=AccountResponse)
def create_account(payload: AccountCreate):
    if ledger.has_account(payload.id):
        raise HTTPException(status_code=400, detail=f"Account '{payload.id}' already exists")

    acct = Account(
        id=payload.id,
        name=payload.name,
        balance=payload.initial_balance
    )
    
    ledger.add_account(acct)
    
    return AccountResponse(
        id=acct.id,
        name=acct.name,
        balance=acct.balance
    )


@app.get("/accounts/{account_id}/balance")
def get_balance(account_id: str) -> dict[str, Any]:
    try:
        balance = ledger.balance(account_id)
    except AccountNotFoundError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    return {"account_id": account_id, "balance": balance}


@app.post("/accounts/{account_id}/deposit")
def deposit(account_id: str, amount: float):
    try:
        tx = ledger.deposit(account_id, amount)
    except (AccountNotFoundError, InvalidAmountError) as exc:
        # 404 if account missing, 400 if invalid amount — we can refine this later
        status = 404 if isinstance(exc, AccountNotFoundError) else 400
        raise HTTPException(status_code=status, detail=str(exc)) from exc

    return {
        "tx_id": tx.tx_id,
        "account_id": tx.account_id,
        "amount": tx.amount,
        "timestamp": tx.timestamp.isoformat(),
    }
