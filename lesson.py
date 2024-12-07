from pydantic import Field
from sqlalchemy import Column, Integer, Sequence, String
from sqlalchemy.orm import declarative_base

from camel_case_model import CamelCaseModel

Base = declarative_base()


class Lesson(Base):
    __tablename__ = "lessons"
    id = Column(Integer, Sequence('lessons_id_seq'), primary_key=True)
    title = Column(String(64), nullable=False)
    video_url = Column(String(512), nullable=True)
    course_id = Column(Integer, nullable=False)
    number = Column(Integer, nullable=False)


class LessonRequestSchema(CamelCaseModel):
    title: str = Field("Урок без темы", max_length=64)
    video_url: str | None = Field(None, max_length=512)
    id: int = None
    course_id: int | None = None
    number: int
