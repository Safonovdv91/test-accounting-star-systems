from datetime import datetime
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import MetaData, Table, Integer, String, TIMESTAMP, ForeignKey, Column, JSON, Boolean


metadata = MetaData()

celestials = Table(
    "celestials",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("age", Integer),
    Column("type_object", Integer, ForeignKey("permitted_types_objects.id")),
    Column("diameter", Integer),
    Column("weight", Integer),
    Column("discription", JSON)
)

stars_systems = Table(
    "stars_systems",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String,),
    Column("age", Integer),
    Column("center_of_mass", Integer, ForeignKey("celestials.id"))
)

types_objects = Table(
    "permitted_types_objects",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
)