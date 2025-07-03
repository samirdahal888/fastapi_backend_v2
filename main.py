from fastapi import FastAPI

from database import create_db_and_tables
from router import admin, student

app = FastAPI(
    title="Student management system",
    description="simple version to keep students data in database",
)


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.get("/")
def home():
    return {"message": "Every thing is OK"}


app.include_router(admin.router)
app.include_router(student.router)
