# app/routes/users.py
from fastapi import APIRouter, HTTPException
from app.models import User
from app import crud

router = APIRouter()

@router.post("/create")
def create_user(user: User):
    existing_user = crud.get_user_by_username(user.username)
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")
    return crud.create_user(user)

@router.get("/{username}")
def get_user(username: str):
    user = crud.get_user_by_username(username)
    if user:
        return user
    raise HTTPException(status_code=404, detail="User not found")
