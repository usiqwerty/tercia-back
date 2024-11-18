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
async def add_course(course: CourseRequestSchema):
    db.add_course(course)

@app.patch('/edit-course')
async def edit_course(course: CourseRequestSchema):
    db.edit_course(course)
