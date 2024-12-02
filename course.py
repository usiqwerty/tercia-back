from pydantic import BaseModel, field_validator
from sqlalchemy import Column, Integer, Sequence, String
from sqlalchemy.orm import declarative_base

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

    @field_validator("name")
    @classmethod
    def name_max_len_64(cls, value):
        if len(value) > 64:
            raise ValueError("Course name length should be less or equal to 64")
        return value

    @field_validator("cover_url")
    @classmethod
    def name_cover_max_len_256(cls, value):
        if len(value) > 256:
            raise ValueError("Coverl URL length should be less or equal to 64")
        return value
