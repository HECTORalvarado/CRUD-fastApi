from fastapi import APIRouter

students = APIRouter()

@students.get("/students")
def getStudents():
    return "Students"


@students.get("/students/{student_id}")
def getStudent(student_id : int):
    return "Students", student_id