from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.dependencies import get_db
from src.services import employee_service
from src.request.employee_request import EmployeeSearchRequest

router = APIRouter()


@router.post("/employee/search")
async def get_posts(search_request: EmployeeSearchRequest, db: AsyncSession = Depends(get_db)):
    return await employee_service.search_employees(search_request, db)
