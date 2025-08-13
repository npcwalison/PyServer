from pydantic import BaseModel # força a tipagem de dados
from typing import Optional

class UserSchemas(BaseModel):
    name: str
    email: str
    passwd: str
    active: Optional[bool]
    admin: Optional[bool]

    class Config:
        from_attributes=True