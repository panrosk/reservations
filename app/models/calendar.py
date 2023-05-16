from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

class EventBase(BaseModel):
    title: str
    description: Optional[str] = None
    start_time: datetime
    end_time: datetime

class EventCreate(EventBase):
    pass

class Event(EventBase):
    id: int
    class Config:
        orm_mode = True
