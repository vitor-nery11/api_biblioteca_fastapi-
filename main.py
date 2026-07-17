from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


livros = []

class Livro(BaseModel):
  titulo:str 
  autor:str 
  paginas:int 
  disponivel:bool
  ano_publicacao:int

# ROTAS GET 
@app.get('/')
def raiz():
    return {'message': 'Ola Mundo!'}


@app.get('/livros')
def listar_livros():
    return livros


@app.get('/livros/{id}')
def buscar_livro(id:int):
    if id < 0 and id >= len(livros):
        raise HTTPException(
            status_code=404,
            detail='Livro não encontrado'
        )

    return livros[id]


# ROTAS POST 
@app.post('/livros')
def criar_livro(livro:Livro):
    livros.append(livro)
    return {
        'mensagem': 'Livro cadastrado com sucesso'
    }


# ROTAS PUT
@app.put('/livros/{id}')
def atualizar_livro(id:int, livro:Livro):
    if id < 0 and id >= len(livros):
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
    if id < 0 and id >= len(livros):
        raise HTTPException(
            status_code=404,
            detail='Livro não encontrado'
        )
    livros.pop(id)
    return {
        'mensagem': 'livro removido'
    }








