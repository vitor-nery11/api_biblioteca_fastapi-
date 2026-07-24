from fastapi import FastAPI, HTTPException,Depends
from sqlalchemy.orm import Session
from schemas.livro import LivroCreate,LivroResponse
from database import Base, engine,SessionLocal,get_db
from models.livro import Livro 
from repositories.livro_repositories import buscar_por_id



app = FastAPI()

livros = []

Base.metadata.create_all(bind=engine)

# ROTAS GET 
@app.get('/')
def raiz():
    return {'message': 'Ola Mundo!'}


@app.get('/livros')
def listar_livros(db:Session = Depends(get_db)):

    return db.query(Livro).all()



@app.get('/livros/{id}')
def buscar_livro(id:int, db: Session = Depends(get_db)):

    livro = buscar_por_id(db, id)

    if livro is None:
        raise HTTPException(
            status_code=404,
            detail='Livro não encontrado'
        )

    return livro


# ROTAS POST 
@app.post('/livros', response_model=LivroResponse)
def criar_livro(livro:LivroCreate, db: Session = Depends(get_db)):

    novo_livro = Livro(
        titulo = livro.titulo,
        autor = livro.autor,
        paginas = livro.paginas,
        disponivel = livro.disponivel,
        ano_publicacao = livro.ano_publicacao
    )
    
    db.add(novo_livro)

    db.commit()

    db.refresh(novo_livro)

    return novo_livro 


# ROTAS PUT
@app.put('/livros/{id}')
def atualizar_livro(id:int, livro:LivroCreate, db: Session = Depends(get_db)):

    livro_db = db.query(Livro).filter(Livro.id == id).first()

    if livro_db is None:
        raise HTTPException(
            status_code=404,
            detail='Livro não encontrado'
        )

    livro_db.titulo = livro.titulo
    livro_db.autor = livro.autor
    livro_db.paginas = livro.paginas
    livro_db.disponivel = livro.disponivel
    livro_db.ano_publicacao = livro.ano_publicacao

    db.commit()
    db.refresh(livro_db)

    return livro_db



# ROTA DELETE 
@app.delete('/livros/{id}')
def deletar_livro(id: int, db: Session = Depends(get_db)):

    livro_db = db.query(Livro).filter(Livro.id == id).first()
    if id < 0 or id >= len(livros):
        raise HTTPException(
            status_code=404,
            detail='Livro não encontrado'
        )

    db.delete(livro_db)
    db.commit()

    return {
        'mensagem': 'livro removido'
    }








