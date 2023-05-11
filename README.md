# Basic CRUD with fastApi

This proyect is a basic implementation of fastapi

## Install the dependences
To install the dependencies, run the following comand

`pip install -r requirements.txt`

## Run the project
To run the project, use the following comand

`uvicorn app:app --reload`

The app will run on `localhost:8000/students`

## Project Structure

```
├── app.py
├── config
│   └── db.py
├── model
│   └── students.py
├── schemas
│   └── students.py
└── README.md
```
* `app.py` FastApi main file
* `routes/students.py` File with the routing and controllers of the API
* `model/students.py` File that contains the model of the database
* `config/db.py` File that manage the config uratin to access the database
* `schemas/students.py` In this file, there are the pydantic models
