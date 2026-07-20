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
    return livros


@app.get('/livros/{id}')
def buscar_livro(id:int):
    if id < 0 or id >= len(livros):
        raise HTTPException(
            status_code=404,
            detail='Livro não encontrado'
        )

    return livros[id]


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
    if id < 0 or id >= len(livros):
        raise HTTPException(
            status_code=404,
            detail='Livro não encontrado'
        )
    livros[id]= livro
    return {
        'mensagem': 'livro atualizado com sucesso'
    }



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








