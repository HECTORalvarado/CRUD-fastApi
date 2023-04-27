from fastapi import APIRouter, status
from schemas.students import Student

students = APIRouter()

@students.get("/students", status_code= status.HTTP_200_OK)
def getStudents():
    return "Students"


@students.get("/students/{student_id}", status_code= status.HTTP_200_OK)
def getStudent(student_id : int):
    return "Students", student_id

@students.post("/students/", status_code= status.HTTP_201_CREATED)
def createStudent( student: Student):
    return 201

@students.put("/students/{student_id}", status_code= status.HTTP_200_OK)
def updateStudent(student_id : int):
    return "Students", student_id

@students.delete("/students/{student_id}", status_code= status.HTTP_200_OK)
def deleteStudent(student_id : int):
    return "Students", student_id