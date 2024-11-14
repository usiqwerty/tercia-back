from pydantic import BaseModel
from sqlalchemy import Column, Integer, Sequence, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Course(Base):
    __tablename__ = "courses"
    id = Column(Integer, Sequence('courses_id_seq'), primary_key=True)
    name = Column(String(64), nullable=False)
    cover_url = Column(String(256), nullable=True)


class CourseRequestSchema(BaseModel):
    name: str
    cover_url: str | None
    id: int = None
