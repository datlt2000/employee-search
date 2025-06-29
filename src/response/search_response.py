from typing import Generic, TypeVar, List
from pydantic import BaseModel

M = TypeVar("M", bound=BaseModel)


class SearchResponse(BaseModel, Generic[M]):
    data: List[M] | None = []
    limit: int | None = 0
    start: int
    total: int
    orderBy: str
    order: str
