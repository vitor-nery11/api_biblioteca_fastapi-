from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


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
def listar_livros(livro:Livro):
   return [
        {
            "titulo": "Dom Casmurro",
            "autor": "Machado de Assis"
        },
        {
            "titulo": "1984",
            "autor": "George Orwell"
        }
    ]


@app.get('/livros/{id}')
def buscar_livro(id:int):
    return {
       'id': id,
    }


# ROTAS POST 
@app.post('/livros')
def criar_livro(livro:Livro):
    return {
        'livro':livro
    }


# ROTAS PUT
@app.put('/livros/{id}')
def atualizar_livro(id:int, livro:Livro):
    return {
        'id':id ,
        'livro':livro
    }


# ROTA DELETE 
@app.delete('/livros/{id}')
def deletar_livro(id: int):
    return {
        'mensagem': 'livro removido',
        'id': id
    }








