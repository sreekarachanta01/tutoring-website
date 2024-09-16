# app/models.py
from pydantic import BaseModel
from typing import List, Optional

class User(BaseModel):
    username: str
    email: str
    is_active: bool = True

class Course(BaseModel):
    title: str
    description: str
    instructor: str
    students: List[str] = []
