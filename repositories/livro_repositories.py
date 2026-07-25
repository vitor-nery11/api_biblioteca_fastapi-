from sqlalchemy.orm import Session
from models.livro import Livro


def buscar_por_id(db: Session, id: int):
    return db.query(Livro).filter(Livro.id == id).first()


def listar_livro(db: Session):
    return db.query(Livro).all()


def criar_livro(db: Session, livro: Livro):
    db.add(livro)
    db.commit()
    db.refresh(livro)
    return livro


def atualizar_livro(db: Session, livro_db: Livro, dados: Livro):
    livro_db.titulo = dados.titulo
    livro_db.autor = dados.autor
    livro_db.paginas = dados.paginas
    livro_db.disponivel = dados.disponivel
    livro_db.ano_publicacao = dados.ano_publicacao

    db.commit()
    db.refresh(livro_db)
    return livro_db


def deletar_livro(db: Session, livro: Livro):
    db.delete(livro)
    db.commit()