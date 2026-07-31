from sqlalchemy.orm import Session
from models.usuario import Usuario


def buscar_usuario_email(db: Session, email: str):
    return db.query(Usuario).filter(
        Usuario.email == email
    ).first()


def criar_usuario(db: Session, usuario: Usuario):
    db.add(usuario)
    db.commit()
    db.refresh(usuario)

    return usuario