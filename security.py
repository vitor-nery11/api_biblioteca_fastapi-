from passlib.context import CryptContext
from jose import jwt
from datetime import datetime,timedelta


SECRET_KEY = 'coloque uma chave grande aqui'

ALGORITHM = 'HS256'

ACCESS_TOKEN_EXPIRE_MINUTES = 30


pwd_context = CryptContext(
    schemes=['bcrypt'],
    deprecated='auto'
)

def gerar_hash(senha:str):
    return pwd_context.hash(senha)

def verificar_senha(senha:str,hash_senha:str):
    return pwd_context.verify(senha,hash_senha)

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




