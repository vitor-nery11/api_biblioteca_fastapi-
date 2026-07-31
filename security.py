from passlib.context import CryptContext
from jose import jwt,JWTError
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException
from datetime import datetime,timedelta
from sqlalchemy.orm import Session
from database import get_db
from repositories.usuario_repositories import buscar_usuario_email



# --

SECRET_KEY = 'coloque uma chave grande aqui'

ALGORITHM = 'HS256'

ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl='login'

)


pwd_context = CryptContext(
    schemes=['bcrypt'],
    deprecated='auto'
)

def gerar_hash(senha:str):
    return pwd_context.hash(senha)

def verificar_senha(senha:str,hash_senha:str):
    return pwd_context.verify(senha,hash_senha)

def get_usuario_logado(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)     
):
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )
        email = payload.get('sub')
        if email is None:
            raise HTTPException(status_code=401, detail="Token inválido")
    except JWTError:
        raise HTTPException(status_code=401, detail="Não autorizado")

    usuario = buscar_usuario_email(
        db,
        email
    )

    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
        
    return usuario



def criar_token(dados: dict):

    dados_token = dados.copy()

    expire = datetime.utcnow() + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    dados_token.update({
        'exp': expire
    }
        
    )

    return jwt.encode(
        dados_token,
        SECRET_KEY,
        algorithm=ALGORITHM
    )






