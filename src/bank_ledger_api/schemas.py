from pydantic import BaseModel
from datetime import datetime
from typing import Any, Literal


class AccountCreate(BaseModel):
    id: str
    name: str | None = None
    initial_balance: float = 0.0


class AccountResponse(BaseModel):
    id: str
    name: str | None = None
    balance: float


class AmountRequest(BaseModel):
    amount: float


class BalanceResponse(BaseModel):
    id: str
    balance: float


class TransactionResponse(BaseModel):
    tx_id: str
    account_id: str
    amount: float
    timestamp: datetime


class ErrorResponse(BaseModel):
    error: str
    message: str
    details: Any | None = None


class TransferRequest(BaseModel):
    from_id: str
    to_id: str
    amount: float
    

class TransferResponse(BaseModel):
    withdraw: TransactionResponse
    deposit: TransactionResponse