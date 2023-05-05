from fastapi import APIRouter, status, Depends, Response
from schemas.students import Student
from sqlalchemy.orm import Session
from config.db import get_db
import model.students

students = APIRouter()

@students.get("/students/", status_code= status.HTTP_200_OK)
def getStudents(db: Session = Depends(get_db)):
    return db.query(model.students.Student).all()

@students.get("/students/{student_id}", status_code= status.HTTP_200_OK)
def getStudent(student_id : int, db: Session = Depends(get_db)):
    estudiante = db.query(model.students.Student).filter(model.students.Student.id_estudiantes == student_id).first()
    if estudiante:
        return estudiante
    else:
        Response.status_code = status.HTTP_404_NOT_FOUND
        return {"messagge":"Estudiante no encontrado"}, 404
        

@students.post("/students/", status_code= status.HTTP_201_CREATED)
def createStudent( student: Student, db: Session = Depends(get_db)):
    student = model.students.Student(
        nombres = student.nombres, 
        apellidos = student.apellidos,
        habilitado = student.habilitado,
        fecha_nacimiento = student.fecha_nacimiento,
        email = student.email,
        telefono = student.telefono)
    db.add(student)
    db.commit()
    db.refresh(student)
    return student

@students.put("/students/{student_id}", status_code= status.HTTP_200_OK)
async def updateStudent(student_id : int, studentUpdate: Student, db: Session = Depends(get_db)):
    student = db.query(model.students.Student).filter(model.students.Student.id_estudiantes == student_id).first()
    if not student:
        Response.status_code = status.HTTP_404_NOT_FOUND
        return {"messagge":"Estudiante no encontrado"}, 404
    else:
        for field, value in studentUpdate.dict().items():
           setattr(student, field, value)
        db.commit()
        db.refresh(student)
        return student

@students.delete("/students/{student_id}", status_code= status.HTTP_200_OK)
def deleteStudent(student_id : int, db: Session = Depends(get_db)):
    student = db.query(model.students.Student).filter(model.students.Student.id_estudiantes == student_id).first()
    if student:
        db.delete(student)
        db.commit()
        return {"messagge":"Estudiante eliminado"}, 200
    else:
        Response.status_code = status.HTTP_404_NOT_FOUND
        return {"messagge":"Estudiante no encontrado"}, 404