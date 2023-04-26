from fastapi import FastAPI

from routes.students import students

app = FastAPI()

app.include_router(students)