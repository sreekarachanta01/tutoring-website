# app/create.py
from app.database import db
from app.models import User, Course

# Users CRUD
def create_user(user: User):
    user_dict = user.dict()
    db["users"].insert_one(user_dict)
    return user_dict

def get_user_by_username(username: str):
    return db["users"].find_one({"username": username}, {"_id": 0})

# Courses CRUD
def create_course(course: Course):
    course_dict = course.dict()
    db["courses"].insert_one(course_dict)
    return course_dict

def get_courses():
    return list(db["courses"].find({}, {"_id": 0}))
