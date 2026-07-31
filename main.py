from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session

from schemas.livro import LivroCreate, LivroResponse
from schemas.usuario import LoginRequest
from database import Base, engine, get_db
from models.livro import Livro
from models.usuario import Usuario  
from security import get_usuario_logado
from schemas.usuario import UsuarioCreate, UsuarioResponse
from services.usuario_service import cadastrar_usuario
from fastapi.security import OAuth2PasswordRequestForm
from services.livro_service import (
    listar_livro,
    buscar_livro,
    criar_livro,
    atualizar_livro,
    deletar_livro,
)
from services.usuario_service import login
from repositories.usuario_repositories import criar_usuario


app = FastAPI()

Base.metadata.create_all(bind=engine)


#  ROTAS GET

@app.get("/")
def raiz():
    return {"message": "Ola Mundo!"}



@app.get("/livros")
def listar_livros_route(db: Session = Depends(get_db)):
    return listar_livro(db)



@app.get("/livros/{id}")
def buscar_livros_route(id: int, db: Session = Depends(get_db)):
    return buscar_livro(db, id)


@app.get('/me', response_model=UsuarioResponse)
def usuario_atual(
    usuario: Usuario = Depends(get_usuario_logado)
):
    return usuario



# ROTAS POST 

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




@app.post("/login")
def fazer_login(
    dados: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    return login(
        db,
        dados.username,
        dados.password
    )

@app.post('/usuarios', response_model=UsuarioResponse)
def cadastrar_usuario_route(
    usuario: UsuarioCreate,
    db: Session = Depends(get_db)
):
    return cadastrar_usuario(
        db,
        usuario.nome,
        usuario.email,
        usuario.senha
    )


# ROTAS PUT 

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



# ROTAS DELETE 

@app.delete("/livros/{id}")
def deletar_livros_route(id: int, db: Session = Depends(get_db)):
    deletar_livro(db, id)
    return {"mensagem": "Livro removido com sucesso"}


