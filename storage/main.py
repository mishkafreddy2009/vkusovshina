from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Integer
from sqlalchemy.sql.sqltypes import String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy. import select

DATABASE_URL = "sqlite+pysqlite:///test.db"

Base = declarative_base()


class Storage(Base):
    __tablename__ = "storages"

    id = Column(Integer, primary_key=True)
    title = Column(String(255), unique=True, nullable=False)
    address = Column(String(255), nullable=False)
    capacity = Column(Integer, nullable=False)


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, nullable=True)
    title = Column(String(255), index=True, unique=True, nullable=False)
    description = Column(String, index=True, nullable=True)
    quantity = Column(Integer, nullable=False)
    # category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    provider_id = Column(Integer, ForeignKey("providers.id"), nullable=False)
    storage_id = Column(Integer, ForeignKey("storages.id"), nullable=False)
    price = Column(Integer, nullable=False)


class Provider(Base):
    __tablename__ = "providers"

    id = Column(Integer, primary_key=True)
    name = Column(String(255))


class Database:
    def __init__(self, database_url):
        self.engine = create_engine(database_url, echo=True, connect_args={"check_same_thread": False})
        self.Session = sessionmaker(bind=self.engine)

    def create_all(self):
        Base.metadata.create_all(self.engine)

    def get_session(self):
        return self.Session()

database = Database(DATABASE_URL)
session = database.get_session()

@asynccontextmanager
async def lifespan(app: FastAPI):
    database.create_all()
    session.add(Provider(
        name="Bebra",
        ))
    session.commit()
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/")
async def hello():
    return {"hello": "world"}
