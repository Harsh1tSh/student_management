# Student Management System API

This project is a **Student Management System API**, built using **FastAPI** and integrated with **MongoDB Atlas** for database storage. It provides a complete backend solution for managing student records.

## Features
- Perform **CRUD operations** (Create, Read, Update, Delete) on student data.
- Integrated with **MongoDB Atlas** for secure and scalable data storage.
- Interactive API documentation available via **Swagger UI**.
- Fully deployed and live on **Render**.

---

## Tech Stack
- **Language**: Python
- **Framework**: FastAPI
- **Database**: MongoDB Atlas (M0 Free Cluster)
- **Server**: Uvicorn ASGI server
- **Deployment**: Render

---

## Live API
The application is deployed and running live at the following URL:  
**Base URL**: [https://student-management-mfyt.onrender.com](https://student-management-mfyt.onrender.com)

### API Documentation
You can explore the API endpoints using the Swagger UI:  
**Swagger UI**: [https://student-management-mfyt.onrender.com/docs](https://student-management-mfyt.onrender.com/docs)

---

## How to Run Locally

### Install dependencies:

```bash
pip install -r requirements.txt
```

### Run the server:

```bash
uvicorn app.main:app --reload
```

### Open the API documentation:

Visit [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to access the interactive API documentation.

## Deployment

The project is deployed on Render. Use the provided base URL to access the live API.


## API Endpoints

**Base URL**: `<Deployed URL>`

| Method | Endpoint       | Description                     |
| ------ | -------------- | ------------------------------- |
| POST   | /students      | Create a new student            |
| GET    | /students      | Get all students (with filters) |
| GET    | /students/{id} | Get a student by ID             |
| PATCH  | /students/{id} | Update a student by ID          |
| DELETE | /students/{id} | Delete a student by ID          |

## Setup Instructions

To run the application, you will need to set up your MongoDB connection. Follow these steps:

1. Create a MongoDB Atlas account and set up a new cluster if you don't have one.
2. Obtain your MongoDB connection URI from the MongoDB Atlas dashboard.
3. Create a `.env` file in the project root and add the following line:
   ```
   MONGO_URI=<your-mongodb-uri>
   ```
4. Replace `<your-mongodb-uri>` with your actual MongoDB connection string.
5. Run the application using:
   ```bash
   uvicorn app.main:app --reload
   ```

You have to create the MongoDB cluster and then connect it with the application
