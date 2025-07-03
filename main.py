from fastapi import FastAPI

from database import create_db_and_tables
from router import admin, student

app = FastAPI(
    title="Student management system",
    description="A secure and lightweight API to manage student records with authentication and full CRUD support.",
    version="1.0.0",
    contact={
        "name": "Samir Dahal",
        "email": "samirdahal217@gmail.com",
        "url": "https://github.com/samirdahal888",
    },
)


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.get("/")
def home():
    return {"message": "Every thing is OK"}


app.include_router(admin.router)
app.include_router(student.router)
