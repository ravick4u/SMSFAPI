from sqlalchemy import Column, Date, DateTime, Integer, String
from database import Base

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    gender = Column(String(10))
    birthday = Column(Date)
    university_name = Column(String(255))
    picture_url = Column(String(255))
    resume_url = Column(String(255))
    created = Column(DateTime)
    created_by = Column(String(255))
    modified = Column(DateTime)
    modified_by = Column(String(255))
