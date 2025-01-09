# models.py
from pydantic import BaseModel
from typing import Optional, Any

class DataResult(BaseModel):
    ok: bool
    result: list
    error: Optional[Any] = None
