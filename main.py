from fastapi import FastAPI, HTTPException
from schemas.livro import LivroCreate,LivroResponse

app = FastAPI()

livros = []

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
    livros.append(livro)
    return livro 


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








