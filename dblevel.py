import os
from typing import Iterable

from sqlalchemy import create_engine, Engine, Connection, select, insert

from course import Course, CourseRequestSchema

HOSTNAME = 'localhost'
PASSWORD = os.environ["POSTGRES_PASS"]
USERNAME = 'terciadb'


class Database:
    engine: Engine
    cursor: Connection

    def __init__(self):
        pass

    def connect(self):
        self.engine = create_engine(f'postgresql://{USERNAME}:{PASSWORD}@{HOSTNAME}/terciadb')  # +psycopg2
        self.cursor = self.engine.connect()

    def get_courses(self) -> Iterable[CourseRequestSchema]:
        for course in self.cursor.execute(select(Course)).scalars():
            yield CourseRequestSchema(id=course.id, name=course.name, cover_url=course.cover_url)

    def add_course(self, course: CourseRequestSchema):
        self.cursor.execute(insert(Course(name=course.name, cover_url=course.cover_url)))
        self.cursor.commit()
