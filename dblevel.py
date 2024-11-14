import os
from typing import Iterable

import sqlalchemy
from sqlalchemy import create_engine, Engine, select
from sqlalchemy.orm import sessionmaker

from course import Course, CourseRequestSchema, Base

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
