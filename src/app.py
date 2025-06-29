from fastapi import FastAPI, APIRouter
import sys
import os

from src.api.v1.employee import employee_api

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from api.v1.employee import employee_api
from src.models.database import Base, engine
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

employee_router = APIRouter(tags=["employee"])

employee_router.include_router(
    employee_api.router,
    tags=["employee"],
    responses={418: {"description": "I'm a teapot"}},
)
app.include_router(employee_router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}
