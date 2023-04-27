from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

database_url = "mysql+pymysql://root@localhost:3306/UFG"

engine = create_engine(database_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()