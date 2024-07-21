from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import router
from app.core.db import init_db, reset_db

origins = [
    "http://localhost:8080",
]


@asynccontextmanager
async def lifespan(app: FastAPI):
    await reset_db()
    await init_db()
    yield


app = FastAPI(lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    # expose_headers=["Content-Range", "Range"]
    expose_headers=["*"],
)
app.include_router(router)
