from pydantic import BaseModel

class AccountCreate(BaseModel):
    id: str
    name: str | None = None
    initial_balance: float = 0.0


class AccountResponse(BaseModel):
    id: str
    name: str | None = None
    balance: float
