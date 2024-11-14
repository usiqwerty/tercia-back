from sqlalchemy import create_engine, Engine
import os
from course import Course

HOSTNAME = 'localhost'
PASSWORD = os.environ["POSTGRES_PASS"]
USERNAME = 'terciadb'


class Database:
    engine: Engine

    def __init__(self):
        pass

    def connect(self):
        self.engine = create_engine(f'postgresql://{USERNAME}:{PASSWORD}@{HOSTNAME}/terciadb') #+psycopg2

    def get_courses(self) -> list[Course]:
        raise NotImplementedError
