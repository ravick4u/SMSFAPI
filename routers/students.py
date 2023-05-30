from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from database.database import get_db
from database.models import Student

from schema.student import StudentCreate
from schema.student import StudentUpdate
from schema.student import StudentResponse

from typing import List

router = APIRouter(
    prefix="/v1/students",
    tags=["Students"]
)

@router.get("/", response_model=List[StudentResponse])
def get_students(database: Session = Depends(get_db)):
    '''Get all students
    '''
    students = database.query(Student).all()

    return students

@router.get('/{id}', response_model=StudentResponse)
def get_student(id: int, database: Session = Depends(get_db)):
    student = database.query(Student).filter(Student.id == id).first()
    if student is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Student with ID {id} not found")
    return student


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=StudentResponse)
#def v2_create_posts(newpost: schema.PostCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
def create_student(newstudent: StudentCreate, database: Session = Depends(get_db)):
    '''Create Student
    '''

    new_student = Student(**newstudent.dict())
    database.add(new_student)
    database.commit()
    database.refresh(new_student)

    print(new_student)
    return new_student

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_student(id: int, db: Session = Depends(get_db)):
    '''Delete Student'''

    student_to_delete_query = db.query(Student).filter(Student.id == id)
    if student_to_delete_query.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Student with {id} not found")
    student_to_delete_query.delete()
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put('/{id}', response_model=StudentResponse)
def update_student(id: int, student: StudentUpdate, db: Session = Depends(get_db)):
    '''Update Student'''

    update_student_query = db.query(Student).filter(Student.id == id)

    if update_student_query.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with {id} not found")

    update_student_query.update(student.dict())
    db.commit()

    return update_student_query.first()