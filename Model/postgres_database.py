import datetime

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


role = Table(
    "role",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("permission", JSON)
)

user = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("email", String, nullable=False),
    Column("username", String, nullable=False),
    Column("hashed_password", String, nullable=False),
    Column("register_at", TIMESTAMP, default=datetime.datetime.utcnow),  # передаем функцию, а не вызываем её
    Column("role_id", Integer, ForeignKey(role.c.id)),
    Column("is_active", Boolean, default=True, nullable=False),
    Column("is_superuser", Boolean, default=False, nullable=False),
    Column("is_verified", Boolean, default=False, nullable=False)
)

# engine = sqlalchemy.create_engine(DATABASE_URL)
# metadata.create_all()

