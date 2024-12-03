from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware

from course import CourseRequestSchema
from dblevel import Database
from lesson import LessonRequestSchema
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

db = Database()
templates = Jinja2Templates(directory="templates")
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


@app.post('/add-lesson')
async def add_lesson(lesson: LessonRequestSchema):
    db.add_lesson(lesson)


@app.get('/get-lesson')
async def get_lesson(lesson_id: int):
    return db.get_lesson(lesson_id)


@app.get('/get-course-lessons')
async def get_course_lessons(course_id: int):
    return list(db.get_course_lessons(course_id))


@app.patch('/edit-lesson')
async def edit_lesson(lesson: LessonRequestSchema):
    db.edit_lesson(lesson)


@app.delete("/delete-course")
async def delete_course(course_id: int):
    db.delete_course(course_id)


@app.delete("/delete-lesson")
async def delete_lesson(lesson_id: int):
    db.delete_course(lesson_id)
