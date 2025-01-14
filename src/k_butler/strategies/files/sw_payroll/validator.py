from typing import TypedDict

from pydantic import BaseModel, EmailStr


class Employee(TypedDict):
    name: str
    email: EmailStr


class SwPayrollValidator(BaseModel):
    emails: dict[str, Employee]
