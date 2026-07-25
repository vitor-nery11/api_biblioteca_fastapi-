from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session

from schemas.livro import LivroCreate, LivroResponse
from database import Base, engine, get_db
from models.livro import Livro
from models.usuario import Usuario
from services.livro_service import (
    listar_livro,
    buscar_livro,
    criar_livro,
    atualizar_livro,
    deletar_livro,
)

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
def raiz():
    return {"message": "Ola Mundo!"}


@app.get("/livros")
def listar_livros_route(db: Session = Depends(get_db)):
    return listar_livro(db)


@app.get("/livros/{id}")
def buscar_livros_route(id: int, db: Session = Depends(get_db)):
    return buscar_livro(db, id)


@app.post("/livros", response_model=LivroResponse)
def criar_livros_route(livro: LivroCreate, db: Session = Depends(get_db)):
    novo = Livro(
        titulo=livro.titulo,
        autor=livro.autor,
        paginas=livro.paginas,
        disponivel=livro.disponivel,
        ano_publicacao=livro.ano_publicacao,
    )
    return criar_livro(db, novo)


@app.put("/livros/{id}")
def atualizar_livros_route(id: int, livro: LivroCreate, db: Session = Depends(get_db)):
    novo = Livro(
        titulo=livro.titulo,
        autor=livro.autor,
        paginas=livro.paginas,
        disponivel=livro.disponivel,
        ano_publicacao=livro.ano_publicacao,
    )
    return atualizar_livro(db, id, novo)


@app.delete("/livros/{id}")
def deletar_livros_route(id: int, db: Session = Depends(get_db)):
    deletar_livro(db, id)
    return {"mensagem": "Livro removido com sucesso"}