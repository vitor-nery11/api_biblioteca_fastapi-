from fastapi import FastAPI, HTTPException
from schemas.livro import LivroCreate,LivroResponse
from database import Base, engine,SessionLocal
from models.livro import Livro 



app = FastAPI()

livros = []

Base.metadata.create_all(bind=engine)

# ROTAS GET 
@app.get('/')
def raiz():
    return {'message': 'Ola Mundo!'}


@app.get('/livros')
def listar_livros():

    db = SessionLocal()

    livros = db.query(Livro).all()

    db.close()

    return livros



@app.get('/livros/{id}')
def buscar_livro(id:int):

    db = SessionLocal()

    livro = db.query(Livro).filter(Livro.id == id).first()

    db.close()

    if livro is None:
        raise HTTPException(
            status_code=404,
            detail='Livro não encontrado'
        )

    return livro


# ROTAS POST 
@app.post('/livros', response_model=LivroResponse)
def criar_livro(livro:LivroCreate):
    db = SessionLocal()

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

    db.close()

    return novo_livro 


# ROTAS PUT
@app.put('/livros/{id}')
def atualizar_livro(id:int, livro:LivroCreate):

    db = SessionLocal()

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
    db.close()

    return livro_db



# ROTA DELETE 
@app.delete('/livros/{id}')
def deletar_livro(id: int):
    if id < 0 or id >= len(livros):
        raise HTTPException(
            status_code=404,
            detail='Livro não encontrado'
        )
    livros.pop(id)
    return {
        'mensagem': 'livro removido'
    }








