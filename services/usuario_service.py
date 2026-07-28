from repositories.usuario_repositories import buscar_usuario_email
from security import verificar_senha, criar_token
from fastapi import HTTPException

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