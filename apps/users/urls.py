# ROTAS ESPECIFICAS
from fastapi import APIRouter, Depends
from core.models import User, db
from sqlalchemy.orm import sessionmaker
from core.utils import catch_session

auth_router = APIRouter(prefix="/auth", tags=["auth"])

#ROTA PRINCIPAL
@auth_router.get("/")
async def home():
    return {"mensagem": "pagina de autenticação!"}


# CRIAR USUARIO
@auth_router.post("/signup")
async def signup(name: str, email: str, passwd: str, session = Depends(catch_session)):
    # Faz um consulta no SQL e compara 
    user = session.query(User).filter(User.email == email).first()
    if user:
        return {"mensagem": "Esse usuario ja testá cadastrado!"}
    else:
        new_user = User(name, email, passwd) # Recebe os dados
        session.add(new_user) # adiciona os dados no banco de dados
        session.commit() # cria o commit para a modificação
        return {"mensagem": "usuário cadastrado com sucesso!"}
