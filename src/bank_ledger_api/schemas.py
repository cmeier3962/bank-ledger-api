from pydantic import BaseModel
from datetime import datetime

class AccountResponse(BaseModel):
    id: str
    name: str | None = None
    balance: float
    
class AccountCreate(BaseModel):
    id: str
    name: str | None = None
    initial_balance: float = 0.0

class DepositRequest(BaseModel):
    amount: float
    
class WithdrawRequest(BaseModel):
    amount: float
    
class BalanceResponse(BaseModel):
    id: str
    balance: float
    
class TransactionReponse(BaseModel):
    tx_id: str
    account_id: str
    amount: str
    timestamp: datetime
    kind: str   # "deposit" | "withdraw" | "transfer"
    
class ErrorResponse(BaseModel):
    pass