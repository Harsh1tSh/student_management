from fastapi import FastAPI
from app.routes import students

app = FastAPI(
    title="Student Management System API",
    description="API for managing students using FastAPI and MongoDB Atlas.",
)


app.include_router(students.router)

@app.get("/")
async def root():
    return {"message": "Welcome to the Student Management System API"}
