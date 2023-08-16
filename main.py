from datetime import datetime
from enum import Enum
from typing import List, Optional

from fastapi import FastAPI
from pydantic import BaseModel, Field

from Model import mongo_database
from Controller import output
from Controller import input

app = FastAPI()

fake_star_systems = [
    {"id": 1, "name": "Solar","age": 35_000, "mass_center": "Sun"},
    {"id": 2, "name": "Sambuka","age": 35_000, "mass_center": "Unknown"},
    {"id": 3, "name": "Wood","age": 35_000, "mass_center": "Tree"},
]

fake_universe_objects = [
    {"id": 1, "name": "Sun", "type": "Star", "age": 100000, "weight": 100123, "diameter": 1231000,
     "star_system": "Solar"},
    {"id": 2, "name": "Tree", "type": "Star", "age": 100001, "weight": 200123, "diameter": 1231001,
     "star_system": "Wood"},
    {"id": 3, "name": "Earth", "type": "Planet", "age": 100121, "weight": 22003, "diameter": 6001,
     "star_system": "Solar"},
    {"id": 4, "name": "1242", "type": "Planet", "age": 100121, "weight": 22003, "diameter": 89001,
     "star_system": "Unknown"},
    {"id": 5, "name": "123", "type": "Planet", "age": 1121, "weight": 22003, "diameter": 1001,
     "star_system": "Unknown"},
    {"id": 6, "name": "55123", "type": "Planet", "age": 1121, "weight": 22003, "diameter": 1001,
     "star_system": "Unknown"},
    {"id": 7, "name": "52511233", "type": "Planet", "age": 1121, "weight": 203, "diameter": 1001,
     "star_system": "Unknown"},
    {"id": 8, "name": "155112323", "type": "Planet", "age": 121, "weight": 22003, "diameter": 101,
     "star_system": "Unknown"},
    {"id": 9, "name": "5251124123", "type": "Planet", "age": 21, "weight": 223, "diameter": 1001,
     "star_system": "Unknown"},
    {"id": 10, "name": "7878251124123", "type": "Planet", "age": 21, "weight": 2003, "diameter": 1001,
     "star_system": "Unknown"},
]


class PermittedTypesCelestialBody(Enum):
    star = "star"
    blackhole = "blackhole"
    blue_gigant = "blue_gigant"
    worm_hole = "worm_hole"
    unknown = "unknown"


class PermittedTypesMassCenter(Enum):
    star = "star"
    blackhole = "blackhole"


class CelestialBody(BaseModel):
    name: str
    age: float | int = Field(ge=0)
    type_object: PermittedTypesCelestialBody = Field()
    diameter: int | float = Field(ge=0)
    weight: int | float = Field(ge=0)
    created_at: datetime


class StarSystem(BaseModel):
    id: int
    name: str
    age: int | float = Field(ge=0)
    mass_center: Optional[CelestialBody]

@app.get("/stars_system/{stars_system_id}", response_model=List[StarSystem])
def get_star_system(stars_system_id):
    return [system for system in fake_star_systems if system.get("id") == int(stars_system_id)]


@app.post("/stars_system/{stars_system_id}")
def rename_star_system(stars_system_id: int, name: str):
    current_star_system =\
        [star_system for star_system in fake_star_systems if star_system["id"] == int(stars_system_id)][0]
    current_star_system["name"] = name
    return {"status": 200, "data": current_star_system}


@app.post("/stars_system_add")
def add_star_system(star_system: List[StarSystem]):
    fake_star_systems.extend(star_system)
    return {"status": 200, "data": fake_star_systems}


@app.get("/universe_objects/", response_model=List[CelestialBody])
def get_universe_objects(limit: int = 3, offset: int = 0):
    return fake_universe_objects[offset:][:limit]
