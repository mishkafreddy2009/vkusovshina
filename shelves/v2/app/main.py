from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.db import reset_db
from core.db import init_db
from api import router


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