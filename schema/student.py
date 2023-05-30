from datetime import date, datetime
from pydantic import BaseModel
from pydantic.schema import Optional

class StudentBase(BaseModel):
    first_name: str
    last_name: str
    gender: str
    birthday: date
    university_name: str
    picture_url: str
    resume_url: str

class StudentCreate(StudentBase):
    pass

class StudentUpdate(StudentBase):
    pass

class StudentResponse(StudentBase):
    id: int
    created: datetime
    created_by: Optional[str]
    modified: datetime
    modified_by: Optional[str]

    class Config:
        orm_mode = True
