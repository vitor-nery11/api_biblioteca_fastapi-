from fastapi import HTTPException
from repositories.livro_repositories import (
    buscar_por_id as repo_buscar_por_id,
    listar_livro as repo_listar_livros,
    criar_livro as repo_criar_livro,
    atualizar_livro as repo_atualizar_livro,
    deletar_livro as repo_deletar_livro,
)


def listar_livro(db):
    return repo_listar_livros(db)


def buscar_livro(db, id: int):
    livro = repo_buscar_por_id(db, id)
    if livro is None:
        raise HTTPException(status_code=404, detail="Livro não encontrado")
    return livro


def criar_livro(db, livro):
    return repo_criar_livro(db, livro)


def atualizar_livro(db, id: int, dados):
    livro_db = repo_buscar_por_id(db, id)
    if livro_db is None:
        raise HTTPException(status_code=404, detail="Livro não encontrado")
    return repo_atualizar_livro(db, livro_db, dados)


def deletar_livro(db, id: int):
    livro = repo_buscar_por_id(db, id)
    if livro is None:
        raise HTTPException(status_code=404, detail="Livro não encontrado")
    repo_deletar_livro(db, livro)