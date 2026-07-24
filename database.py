from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase,sessionmaker,Session



DATABASE_URL = 'sqlite:///biblioteca.db'

engine = create_engine(DATABASE_URL)

class Base(DeclarativeBase):
  pass


SessionLocal = sessionmaker(bind=engine)

def get_db():
    db = SessionLocal()

    try:
       yield db 

    finally:
       db.close()

