from pydantic import BaseModel, Required, EmailStr
from fastapi import Query, Path
from typing import Annotated

class Student (BaseModel):
    id: Annotated[int, None, Query(
        title= "ID",
        description= "ID del estudiante")]
    name: Annotated[str, Query(
        title= "Nombre",
        description= "Nombre del estudiante",
		max_length=75)] = Required
    lastName: Annotated[str, Query(
        title= "Apellido",
        description= "Apellido del estudiante",
		max_length=100)] = Required
    habilitado: Annotated[int, Path(
        title= "Habilitado",
        description= "Estado del estudiante, puede ser 1 o 0",
        ge= 0,
        le= 1
        )] = 0
    email: Annotated[EmailStr, Query(
        title= "Correo electronico",
        description= "Correo electronico del estudiante")] = Required
    date: Annotated[str, Query(
        title= "Fecha de nacimiento",
        description= "Fecha de nacimiento del estudiante",
		regex=r'^\d{2}-\d{2}-\d{4}$')] = Required
    phone: Annotated[str, Query(
        title= "Telefono",
        description= "Telefono del estudiante",
		regex=r'^\d{4}-\d{4}$')] = Required