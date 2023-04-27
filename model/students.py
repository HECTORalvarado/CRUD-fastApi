from sqlalchemy import Column, DefaultClause, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
    __tablename__ = "estudiantes"

    id_estudiantes = Column(Integer, primary_key=True, index=True)
    nombres = Column(String(75), unique=False)
    apellidos = Column(String(100), unique=False)
    habilitado = Column(Boolean, nullable=False, server_default=DefaultClause("false"))
    fecha_nacimiento = Column(String, unique=False)
    email = Column(String, unique=False)
    telefono = Column(String, unique=False)