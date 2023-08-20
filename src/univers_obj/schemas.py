from datetime import datetime

from pydantic import BaseModel


class UniverseObjectCreate(BaseModel):
    cbodyId: int
    name: str
    age: int
    star_system: int
    type_object: int
    diameter: int
    weight: int
    additing_date: datetime
    discription: str
