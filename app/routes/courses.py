# app/routes/courses.py
from fastapi import APIRouter
from app.models import Course
from app import crud

router = APIRouter()

@router.post("/create")
def create_course(course: Course):
    return crud.create_course(course)

@router.get("/")
def get_all_courses():
    return crud.get_courses()
