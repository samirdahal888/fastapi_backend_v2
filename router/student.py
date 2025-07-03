from fastapi import APIRouter,Depends,HTTPException,status
from typing import Annotated
from module import Admin,StudenCreate,Student,StudentUpdate
from oauth2 import get_current_user
from database import SessionDep
from sqlmodel import select


router = APIRouter(tags=['STUDENTS'])

@router.get('/student')
def get_students(current_admin: Annotated[Admin, Depends(get_current_user)],session:SessionDep):
    statement = select(Student)
    students = session.exec(statement).all()
    return students

@router.post('/student')
def create_sudent(current_admin: Annotated[Admin, Depends(get_current_user)],request:StudenCreate,session:SessionDep):
    student_db = Student.model_validate(request)
    session.add(student_db)
    session.commit()
    session.refresh(student_db)
    return student_db

@router.delete('/student/{student_id}')
def delet_user(current_admin: Annotated[Admin, Depends(get_current_user)],session:SessionDep,student_id):
    student = session.get(Student,student_id)
    if not student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='student not found')
    session.delete(student)
    session.commit()
    return f"student deleted of id {student_id}"


@router.patch("/student/{student_id}")
def update_sutdent(current_admin: Annotated[Admin, Depends(get_current_user)],session:SessionDep,student_id,student:StudentUpdate):
    old_student_deails = session.get(Student,student_id)
    if not student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Student is not in Database")
    
    new_student_details = student.model_dump(exclude_unset=True)
    old_student_deails.sqlmodel_update(new_student_details)
    session.add(old_student_deails)
    session.commit()
    session.refresh(old_student_deails)
    return old_student_deails





    





