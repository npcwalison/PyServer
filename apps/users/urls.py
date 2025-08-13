# ROTAS ESPECIFICAS
from fastapi import APIRouter, Depends, HTTPException
from core.models import User, db
from sqlalchemy.orm import sessionmaker, Session
from core.utils import catch_session
from main import bcrypt_context

from apps.users.schemas import UserSchemas

auth_router = APIRouter(prefix="/auth", tags=["auth"])

#ROTA PRINCIPAL
@auth_router.get("/")
async def home():
    return {"mensagem": "pagina de autenticação!"}

# trocar os dados pelos valosers no UseSchemas
#useschemas: UseSchemas

# CRIAR USUARIO
@auth_router.post("/signup")
async def signup(name: str, email: str, passwd: str, session: Session = Depends(catch_session)):
    # Faz um consulta no SQL e compara 
    user = session.query(User).filter(User.email == email).first()
    if user:
        # raise no lugar de return, ele levanta o erro no lugar de retornar.
        raise HTTPException(status_code=400, detail="Usuario já cadastrado")
    else:
        passwd_encrypted = bcrypet_context.hash(passwd)
        new_user = User(name, email, passwd_encrypted)   # Recebe os dados
        session.add(new_user) # adiciona os dados no banco de dados
        session.commit() # cria o commit para a modificação
        return {"mensagem": f"usuário cadastrado com sucesso! {email}"}
