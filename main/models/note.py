import time
from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class Note(BaseModel):
    id: int
    title: str
    content: str
    created_at: datetime
