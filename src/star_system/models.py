from datetime import datetime

from sqlalchemy import Column, Table, Integer, String, ForeignKey, TIMESTAMP

from database import metadata

star_system = Table(
    "star_system",
    metadata,
    Column("systemId", Integer, primary_key=True),
    Column("name", String),
    Column("age", Integer),
    Column("center_of_mass", Integer, ForeignKey("celestial_body.cbodyId"), default=None),
    Column("additing_date", TIMESTAMP, default=datetime.utcnow())
)
