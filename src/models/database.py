from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Date
from datetime import datetime

SQLALCHEMY_DATABASE_URL = "sqlite+aiosqlite:///./db.sqlite3"
# SQLALCHEMY_DATABASE_URL = "postgresql://guest:password@postgresserver/db"

engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = async_sessionmaker(engine)

Base = declarative_base()

class Model(Base):
    __abstract__ = True
    createdAt = Column(Date, default=datetime.now)
    updatedAt = Column(Date, onupdate=datetime.now)
    def update(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)