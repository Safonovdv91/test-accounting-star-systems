import datetime

from sqlalchemy import MetaData, Table, Integer, String, TIMESTAMP, ForeignKey, Column, JSON

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


roles = Table(
    "roles",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("permission", JSON)
)

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("email", String, nullable=False),
    Column("username", String, nullable=False),
    Column("password", String, nullable=False),
    Column("register_at", TIMESTAMP, default=datetime.datetime.utcnow),  # передаем функцию, а не вызываем её
    Column("role_id", Integer, ForeignKey("roles.id"))
)

# engine = sqlalchemy.create_engine(DATABASE_URL)
# metadata.create_all()

