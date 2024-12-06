import os
from motor.motor_asyncio import AsyncIOMotorClient

# MongoDB Atlas connection URI
MONGO_URI = #here yu will entreryour mongodb uri

# Connect to the database
client = AsyncIOMotorClient(MONGO_URI)
db = client.student_management
students_collection = db.students
