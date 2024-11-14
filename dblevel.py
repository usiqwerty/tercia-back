from typing import Iterable

from sqlalchemy import create_engine, Engine, Connection, select
import os
from course import Course

HOSTNAME = 'localhost'
PASSWORD = os.environ["POSTGRES_PASS"]
USERNAME = 'terciadb'


class Database:
    engine: Engine
    cursor: Connection
    def __init__(self):
        pass

    def connect(self):
        self.engine = create_engine(f'postgresql://{USERNAME}:{PASSWORD}@{HOSTNAME}/terciadb') #+psycopg2
        self.cursor = self.engine.connect()

    def get_courses(self) -> Iterable[Course]:
        return self.cursor.execute(select(Course)).scalars()
