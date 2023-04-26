from fastapi import FastAPI

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    print('hello world')