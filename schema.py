from datetime import date, datetime
from pydantic import BaseModel

class StudentBase(BaseModel):
    '''Student Base Class'''
    
    first_name: str
    last_name: str
    gender: str
    birthday: date
    university_name: str
    picture_url: str
    resume_url: str
    


class StudentCreate(StudentBase):
    '''Student Class to be used in Create'''
    pass


class StudentUpdate(StudentBase):
    '''Student class to be used in Update'''
    pass


class Student(StudentBase):
    '''Student class to be used in returning data'''
    id: int
    created: datetime
    created_by: str
    modified: datetime
    modified_by: str

    class Config:
        orm_mode = True

