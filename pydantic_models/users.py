from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class PydanticNote(BaseModel):
    id: int
    title: str
    description: str


class PydanticUserAccount(BaseModel):
    id: int
    first_name: str
    last_name: str


class PydanticUser(BaseModel):
    id: int
    username: str
    updated_at: datetime
    notes: list["PydanticNote"]
    account: "PydanticUserAccount"
