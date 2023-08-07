from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class User(BaseModel):
    name: str
    last_name: str
    email: str
    phone: str
    address: Optional[str]
    created_at: datetime = datetime.now()

