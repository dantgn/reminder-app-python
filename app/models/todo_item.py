from typing import Optional
from pydantic import BaseModel

class TodoItem(BaseModel):
    id: Optional[int]
    title: str
    description: str
