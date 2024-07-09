from databases import Database
from sqlalchemy import Column, Integer, MetaData, String, Table, create_engine

DATABASE_URL = "postgresql://postgres:postgres@localhost/vkusovshina"

engine = create_engine(DATABASE_URL)
metadata = MetaData()

storages = Table(
    "storages",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String(255)),
    Column("address", String(255)),
    Column("phone_number", String(255)),
)

database = Database(DATABASE_URL)
