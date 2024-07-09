from os import getenv
from databases import Database
from sqlalchemy import (MetaData, Table, Column,
                         String, Integer, create_engine)


DATABASE_URL = f"postgresql+asyncpg://postgres:{getenv('postgresql_pass')}@localhost/vkusovshina"

engine = create_engine(DATABASE_URL)
metadata = MetaData()

shelves = Table(
    "shelves",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("shelf_type", String(255)),
    Column("volume", Integer),
)

database = Database(DATABASE_URL)
