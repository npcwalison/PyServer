from pydantic import BaseModel # força a tipagem de dados
from typing import Optional

class UserSchema(BaseModel):
    name: str
    email: str
    passwd: str
    active: Optional[bool]
    admin: Optional[bool]

    class Config:
        from_attributes=True

class RequestSchema(BaseModel):
    user: int

    class Config:
        from_attributes = True

class SignInSchema(BaseModel):
    email: str
    passwd: str

    class Config:
        from_attributes = True