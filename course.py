from pydantic import BaseModel, Field
from sqlalchemy import Column, Integer, Sequence, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Course(Base):
    __tablename__ = "courses"
    id = Column(Integer, Sequence('courses_id_seq'), primary_key=True)
    name = Column(String(64), nullable=False)
    cover_url = Column(String(256), nullable=True)


class CourseRequestSchema(BaseModel):
    name: str = Field("Безымянный курс", max_length=64)
    cover_url: str | None = Field(None, max_length=256)
    id: int = None
