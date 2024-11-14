import os
from typing import Iterable

import sqlalchemy
from sqlalchemy import create_engine, Engine, Connection, select, insert, table, Table
from sqlalchemy.orm import sessionmaker

from course import Course, CourseRequestSchema, Base

HOSTNAME = 'localhost'
PASSWORD = os.environ["POSTGRES_PASS"]
USERNAME = 'terciadb'


class Database:
    engine: Engine
    # cursor: Connection
    session: sqlalchemy.orm.Session
    table: Table

    def __init__(self):
        pass

    def connect(self):
        self.engine = create_engine(f'postgresql://{USERNAME}:{PASSWORD}@{HOSTNAME}/terciadb')  # +psycopg2
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        # self.cursor = self.engine.connect()
        self.session = Session()

        self.table = Base.metadata.tables["courses"]

    def get_courses(self) -> Iterable[CourseRequestSchema]:
        query = select(Course)
        for course in self.session.execute(query).scalars():
            yield CourseRequestSchema(id=course.id, name=course.name, cover_url=course.cover_url)

    def add_course(self, course: CourseRequestSchema):
        # query = insert().values(name=course.name, cover_url=course.cover_url)

        self.session.add(Course(name=course.name, cover_url=course.cover_url))
        self.session.commit()
