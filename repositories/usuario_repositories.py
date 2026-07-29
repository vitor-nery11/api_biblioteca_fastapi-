from sqlalchemy.orm import Session
from database import get_db
from repositories.usuario_repositories import buscar_usuario_email
from models.usuario import Usuario

def buscar_usuario_email(db:Session, email:str):
    return db.query(Usuario).filter(
        Usuario.email == email
    ).first()
