from datetime import datetime

from pydantic import BaseModel


class StarSystemCreate(BaseModel):
    # systemId: int
    name: str
    age: int
    center_of_mass: int
    additing_date: datetime


