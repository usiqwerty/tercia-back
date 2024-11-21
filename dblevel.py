import os
from typing import Iterable

import sqlalchemy
from sqlalchemy import create_engine, Engine, select
from sqlalchemy.orm import sessionmaker

from course import Course, CourseRequestSchema, Base
from lesson import LessonRequestSchema, Lesson

HOSTNAME = 'localhost'
PASSWORD = os.environ["POSTGRES_PASS"]
USERNAME = 'terciadb'
DB_NAME = 'terciadb'


class Database:
    engine: Engine
    session: sqlalchemy.orm.Session

    def __init__(self):
        pass

    def connect(self):
        self.engine = create_engine(f'postgresql://{USERNAME}:{PASSWORD}@{HOSTNAME}/{DB_NAME}')
        Base.metadata.create_all(self.engine)
        self.session = sessionmaker(bind=self.engine)()

    def get_courses(self) -> Iterable[CourseRequestSchema]:
        query = select(Course)
        for course in self.session.execute(query).scalars():
            yield CourseRequestSchema(id=course.id, name=course.name, cover_url=course.cover_url)

    def add_course(self, course: CourseRequestSchema):
        self.session.add(Course(name=course.name, cover_url=course.cover_url))
        self.session.commit()

    def edit_course(self, course: CourseRequestSchema):
        old_course_query = select(Course).where(Course.id == course.id)
        old_course = self.session.execute(old_course_query).scalars().first()
        old_course.name = course.name
        old_course.cover_url = course.cover_url
        self.session.commit()

    def add_lesson(self, lesson: LessonRequestSchema):
        sql_lesson = Lesson(title=lesson.title, video_url=lesson.video_url, course_id=lesson.course_id)
        self.session.add(sql_lesson)
        self.session.commit()

    def get_lesson(self, lesson_id: int):
        query = select(Lesson).where(Lesson.id == lesson_id)
        lesson = self.session.execute(query).scalars().first()
        return LessonRequestSchema(id=lesson.id, title=lesson.title, video_url=lesson.video_url, course_id=lesson.course_id)

    def get_course_lessons(self, course_id:int):
        query = select(Lesson).where(Lesson.course_id == course_id)
        for lesson in self.session.execute(query).scalars():
            yield LessonRequestSchema(id=lesson.id, title=lesson.title, video_url=lesson.video_url,
                                   course_id=lesson.course_id)

    def edit_lesson(self, lesson: LessonRequestSchema):
        old_lesson_query = select(Lesson).where(Lesson.id == lesson.id)
        old_lesson = self.session.execute(old_lesson_query).scalars().first()
        old_lesson.title = lesson.title
        old_lesson.video_url = lesson.video_url
        self.session.commit()
