from datetime import datetime
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import MetaData, Table, Integer, String, TIMESTAMP, ForeignKey, Column, JSON, Boolean

from database import metadata

# metadata = MetaData() - используем из database, что бы все данные от табл хранились в одном месте

celestials = Table(
    "celestial_body",
    metadata,
    Column("cbodyId", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("age", Integer),
    # Column("star_system", Integer, ForeignKey("star_system.systemId")),
    Column("star_system", Integer),
    Column("type_object", Integer, ForeignKey("permitted_type_object.Id")),
    Column("diameter", Integer),
    Column("weight", Integer),
    Column("additing_date", TIMESTAMP, default=datetime.utcnow()),
    Column("discription", String)

)

permitted_type_object = Table(
    "permitted_type_object",
    metadata,
    Column("Id", Integer, primary_key=True),
    Column("name", String, nullable=False),
)
