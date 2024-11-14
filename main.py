from fastapi import FastAPI

from course import Course, CourseRequestSchema
from dblevel import Database

app = FastAPI()
db = Database()
db.connect()


@app.get("/get-courses")
async def root():
    return list(db.get_courses())


@app.post("/add-course")
async def root(course: CourseRequestSchema):
    db.add_course(course)
