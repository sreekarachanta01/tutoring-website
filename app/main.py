from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from bson import ObjectId

app = FastAPI()

# Connect to MongoDB - also can be database.py(seperate file)
client = MongoClient("mongodb://localhost:27017")
db = client["tutoring_db"]


# Helper function to convert MongoDB ObjectId to string
def serialize_dict(doc):
    """
    Converts MongoDB document (with ObjectId) to a serializable dict
    """
    return {**doc, "_id": str(doc["_id"])}



@app.post("/users/create")
async def create_user(user: dict):
    try:
        # Insert the user data into the MongoDB "users" collection
        result = db.users.insert_one(user)
        # Fetch the newly created user document
        new_user = db.users.find_one({"_id": result.inserted_id})
        # Return the serialized version of the new user (converting ObjectId to string)
        return serialize_dict(new_user)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating user: {str(e)}")

@app.get("/users/{username}")
async def get_user(username: str):
    user = db.users.find_one({"username": username})
    if user:
        return serialize_dict(user)
    else:
        raise HTTPException(status_code=404, detail="User not found")

@app.post("/courses/create")
async def create_course(course: dict):
    try:
        # Insert the course data into the MongoDB "courses" collection
        result = db.courses.insert_one(course)
        # Fetch the newly created course document
        new_course = db.courses.find_one({"_id": result.inserted_id})
        # Return the newly created course
        return {"course": serialize_dict(new_course)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating course: {str(e)}")
    
@app.get("/courses/")
async def get_courses():
    try:
        # Fetch all courses from the "courses" collection
        courses = db.courses.find()
        # Convert courses to a list of dictionaries
        course_list = [serialize_dict(course) for course in courses]
        return {"courses": course_list}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching courses {str(e)}")
    
