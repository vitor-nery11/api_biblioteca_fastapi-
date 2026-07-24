from sqlalchemy.orm import Session
from models.livro import Livro 

def bsucar_por_id(db: Session, id:int ):
    
    return db.query(Livro).filter(Livro.id == id).first()
