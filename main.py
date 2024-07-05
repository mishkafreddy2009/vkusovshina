from fastapi import FastAPI
from starlette.responses import JSONResponse
from contextlib import asynccontextmanager
from storage.models import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/")
async def hello():
    return {"hello", "wolrd"}
