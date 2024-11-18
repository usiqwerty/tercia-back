from pydantic import BaseModel
from sqlalchemy import Column, Integer, Sequence, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Lesson(Base):
    __tablename__ = "lessons"
    id = Column(Integer, Sequence('lessons_id_seq'), primary_key=True)
    title = Column(String(64), nullable=False)
    video_url = Column(String(512), nullable=True)
    course_id = Column(Integer, nullable=False)


class LessonRequestSchema(BaseModel):
    title: str
    video_url: str | None
    id: int = None
    course_id :int|None = None