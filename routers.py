from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
import schema
import models

router = APIRouter(
    prefix="/v1/students",
    tags=["Students"]
)

@router.get('/{id}', response_model=schema.Student)
def get_student(id: int, db: Session = Depends(get_db)):
    '''Get single student'''
    
    return_student = db.query(models.Student).filter(models.Student.id == id).first()

    if return_student is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Studnet with {id} not found")
    else:
        return return_student