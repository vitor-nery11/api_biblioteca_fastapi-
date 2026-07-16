from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Livro(BaseModel):
  titulo:str 
  autor:str 
  paginas:int 
  disponivel:str

# ROTAS GET 
@app.get('/livros')
def listar_livros(livro:Livro):
    return {
       'titulo': livro,
       'autor': livro
    }


@app.get('/livros/{id}')
def buscar_livro(id:int,livro:Livro):
    return {
       'id': id,
       'livro':livro
    }




