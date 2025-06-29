from pydantic import BaseModel


class SearchRequest(BaseModel):
    start: int | None
    limit: int | None
    orderBy: str = "id"
    order: str = "desc"
