# Tutoring API
This project is a simple API model for managing courses and users in tutoring system, built using Fast API and MongoDB. The API allows you to perform basic tutoring website operations as a backend program on users and courses.

## Features
**Create and Fetch users**:
 - Create a new user with `users/create/` endpoint.
 - Fetch a user by their username using the `/users/{username}` endpoint.

 **Create and Fetch users**:
 - create a new course with the `/courses/create` endpoint.
 - Fetch a list of all courses using the `/courses/` endpoint.

 ## Project Structure

 The project consists of two main parts:
- **API Endpoints**: FastAPI is used to create RESTful endpoints for managing users and courses.
- **MongoDB**: MongoDB is used as the database to store user and course information.

### Files:
- `main.py`: The FastAPI application with route handlers for managing users and courses.
- `database.py` (optional): A separate file that can be used for handling MongoDB connections.

### MongoDB Connection

The app connects to a MongoDB instance running locally at `mongodb://localhost:27017` and uses the database `tutoring_db`. Make sure MongoDB is installed and running before starting the application.

## API Endpoints

### Users

- **Create User**  
  `POST /users/create`  
  Accepts a JSON object representing the user and inserts it into the `users` collection.

  **Example Request:**
  ```json
  {
    "username": "johndoe",
    "email": "johndoe@example.com",
    "age": 25
  }

**Response:**
```json

{
  "_id": "605c70f879b34815d0c66d4f",
  "username": "johndoe",
  "email": "johndoe@example.com",
  "age": 25
}

