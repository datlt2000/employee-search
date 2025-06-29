from fastapi import HTTPException, UploadFile
from fastapi.responses import FileResponse
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, text, func
from src.models.employees import Employees
from src.response.employee_response import EmployeeResponse
from src.request.employee_request import EmployeeSearchRequest
from src.response.search_response import SearchResponse


async def get_employees(search_request: EmployeeSearchRequest, db: AsyncSession) -> list[EmployeeResponse]:
    results = await db.execute(select(Employees)
                               .order_by(text(search_request.orderBy + " " + search_request.order))
                               .offset(search_request.start)
                               .limit(search_request.limit))
    employees = results.scalars().all()
    return [EmployeeResponse.model_validate(employee, from_attributes=True, strict=True) for employee in employees]


async def count_employee(search_request: EmployeeSearchRequest, db: AsyncSession) -> int:
    count_result = await db.execute(select(func.count(Employees.id)).select_from(Employees))
    count = count_result.scalar()
    return count


async def search_employees(search_request: EmployeeSearchRequest, db: AsyncSession) -> SearchResponse[EmployeeResponse]:
    employees = await get_employees(search_request, db)
    count = await count_employee(search_request, db)
    search_response = SearchResponse(
        **search_request.model_dump(), data=employees, total=count)
    return search_response
