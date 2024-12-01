from fastapi import APIRouter, HTTPException
from bson import ObjectId
from app.models import Student
from app.database import students_collection

router = APIRouter() 

# Helper function to convert MongoDB object to JSON
def student_helper(student) -> dict:
    return {
        "id": str(student["_id"]),
        "name": student["name"],
        "age": student["age"],
        "address": student["address"],
    }

# Create a new student
@router.post("/students", status_code=201)
async def create_student(student: Student):
    student_dict = student.dict()
    result = await students_collection.insert_one(student_dict)
    return {"id": str(result.inserted_id)}

# Get a list of students (with optional filters)
@router.get("/students")
async def list_students(country: str = None, age: int = None):
    query = {}
    if country:
        query["address.country"] = country
    if age:
        query["age"] = {"$gte": age}

    students = await students_collection.find(query).to_list(100)
    return {"data": [student_helper(student) for student in students]}

# Get a single student by ID
@router.get("/students/{id}")
async def fetch_student(id: str):
    student = await students_collection.find_one({"_id": ObjectId(id)})
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student_helper(student)

# Update a student by ID
@router.patch("/students/{id}", status_code=204)
async def update_student(id: str, student: Student):
    update_data = {key: value for key, value in student.dict(exclude_unset=True).items()}
    result = await students_collection.update_one(
        {"_id": ObjectId(id)}, {"$set": update_data}
    )
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Student not found")
    return

# Delete a student by ID
@router.delete("/students/{id}")
async def delete_student(id: str):
    result = await students_collection.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"message": "Student deleted successfully"}
