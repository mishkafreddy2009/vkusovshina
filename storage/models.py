from typing_extensions import Annotated

from sqlalchemy.engine import create_engine
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Integer
from sqlalchemy.sql.sqltypes import String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

Base = declarative_base()


class Storage(Base):
    __tablename__ = "storages"

    id = Column(Integer, primary_key=True)
    title = Column(String(255), unique=True)
    address = Column(String(255), nullable=True)
    capacity = Column(Integer)


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    title = Column(String(255), index=True, unique=True)
    description = Column(String, index=True)
    product_category = Column(String(255), index=True)
    quantity = Column(Integer)
    provider_id = Column(Integer, ForeignKey("providers.id")) 
    storage_id = Column(Integer, ForeignKey("storages.id"))
    price = Column(Integer)


class Provider(Base):
    __tablename__ = "providers"

    id = Column(Integer, primary_key=True)


def init_db():
    engine = create_engine("sqlite+pysqlite:///test.db", echo=True)

    Base.metadata.create_all(engine)

    with Session(engine) as session:
        pr1 = Product(
                title="Сникерс",
                description="Чоколатка",
                product_category="Шоколад",
                quantity=450,
                provider_id=3,
                storage_id=0,
                price=5000,
                )
        session.add(pr1)
        session.commit()
