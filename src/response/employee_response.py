from pydantic import BaseModel
from typing import List
from src.const.enum import POST_STATUS
from datetime import date


class EmployeeResponse(BaseModel):
    id: int
    title: str
    status: POST_STATUS
    description: str | None
    content: str | None
    createdAt: date
