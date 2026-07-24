from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase,sessionmaker,Session

def get_db():
    db = SessionLocal()

    try:
       yield db 

    finally:
       db.close()


DATABASE_URL = 'sqlite:///biblioteca.db'

engine = create_engine(DATABASE_URL)

class Base(DeclarativeBase):
  pass


SessionLocal = sessionmaker(bind=engine)

