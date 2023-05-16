from pydantic import BaseModel
from uuid import uuid4
import datetime

class Item(BaseModel):
    id: str
    label: str
    create_ts: datetime.datetime