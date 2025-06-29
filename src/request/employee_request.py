from src.request.search_request import SearchRequest


class EmployeeSearchRequest(SearchRequest):
    email: str
    first_name: str
    last_name: str
    password: str
