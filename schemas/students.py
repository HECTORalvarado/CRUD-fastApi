from pydantic import BaseModel, Required, EmailStr
from fastapi import Query
from typing import Annotated

class Student (BaseModel):
    id: Annotated[int, None, Query(
        title= "ID",
        description= "ID del estudiante")] = None
    nombres: Annotated[str, Query(
        title= "Nombre",
        description= "Nombre del estudiante",
		max_length=75)] = Required
    apellidos: Annotated[str, Query(
        title= "Apellido",
        description= "Apellido del estudiante",
		max_length=100)] = Required
    habilitado: Annotated[bool, Query(
        title= "Habilitado",
        description= "Estado del estudiante, puede ser True o False",
        )] = False
    email: Annotated[EmailStr, Query(
        title= "Correo electronico",
        description= "Correo electronico del estudiante")] = Required
    fecha_nacimiento: Annotated[str, Query(
        title= "Fecha de nacimiento",
        description= "Fecha de nacimiento del estudiante",
		regex=r'^\d{4}-\d{2}-\d{2}$')] = Required
    telefono: Annotated[str, Query(
        title= "Telefono",
        description= "Telefono del estudiante",
		regex=r'^\d{4}-\d{4}$')] = Required