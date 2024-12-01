import os
from motor.motor_asyncio import AsyncIOMotorClient

# MongoDB Atlas connection URI
MONGO_URI = "mongodb+srv://admin:adminpassword123@cluster0.1kadn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Connect to the database
client = AsyncIOMotorClient(MONGO_URI)
db = client.student_management
students_collection = db.students
