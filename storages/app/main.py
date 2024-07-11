from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from app.core.db import get_session, reset_db
from app.core.db import init_db
from app.models.models import Storage
from app.models.models import StorageCreate
from app.models.models import Product
from app.models.models import ProductCreate
from app.api import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await reset_db()
    await init_db()
    yield


app = FastAPI(lifespan=lifespan)

app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:8080"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
        )

app.include_router(router)
