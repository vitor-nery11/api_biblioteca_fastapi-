from fastapi import HTTPException
from models.usuario import Usuario

from repositories.usuario_repositories import (
    buscar_usuario_email,
    criar_usuario
)

from security import (
    verificar_senha,
    criar_token,
    gerar_hash
)


def cadastrar_usuario(db, nome, email, senha):

    usuario_existente = buscar_usuario_email(db, email)

    if usuario_existente:
        raise HTTPException(
            status_code=400,
            detail="Email já cadastrado"
        )

    senha_hash = gerar_hash(senha)

    usuario = Usuario(
        nome=nome,
        email=email,
        senha=senha_hash
    )

    return criar_usuario(db, usuario)


def login(db, email, senha):

    usuario = buscar_usuario_email(db, email)

    if usuario is None:
        raise HTTPException(
            status_code=401,
            detail="Email ou senha inválidos"
        )

    if not verificar_senha(
        senha,
        usuario.senha
    ):
        raise HTTPException(
            status_code=401,
            detail="Email ou senha inválidos"
        )

    token = criar_token(
        {
            "sub": usuario.email
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }