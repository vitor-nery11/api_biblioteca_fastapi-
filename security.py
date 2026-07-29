from passlib.context import CryptContext
from jose import jwt,JWTError
from fastapi.security import OAuth2AuthorizationCodeBearer
from fastapi import Depends
from datetime import datetime,timedelta
from sqlalchemy.orm import Session
from database import get_db
from repositories.usuario_repositories import buscar_usuario_email



# --

SECRET_KEY = 'coloque uma chave grande aqui'

ALGORITHM = 'HS256'

ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2AuthorizationCodeBearer(
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
    payload = jwt.decode(
        token,
        SECRET_KEY,
        algorithms=[ALGORITHM]
    )

    email = payload.get('sub')

    usuario = buscar_usuario_email(
        db,
        email
    )

    print(usuario)



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






