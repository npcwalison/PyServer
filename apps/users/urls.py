# ROTAS ESPECIFICAS
from fastapi import APIRouter, Depends, HTTPException
from core.models import User, db
from sqlalchemy.orm import sessionmaker, Session
from core.utils import catch_session
from main import bcrypt_context

from apps.users.schemas import UserSchema, SignInSchema

auth_router = APIRouter(prefix="/auth", tags=["auth"])

# funcao para criar um token no login
def crate_token(email):
    token = f"jsd43HG359HGhsv{email}"
    return token

#ROTA PRINCIPAL
@auth_router.get("/")
async def home():
    return {"mensagem": "pagina de autenticação!"}

# trocar os dados pelos valosers no UseSchemas
#useschemas: UserSchemas

# CRIAR USUARIO
@auth_router.post("/signup")
async def signup(useschema: UserSchema, session: Session = Depends(catch_session)):
    # Faz um consulta no SQL e compara 
    user = session.query(User).filter(User.email == useschema.email).first()
    if user:
        # raise no lugar de return, ele levanta o erro no lugar de retornar.
        raise HTTPException(status_code=400, detail="Usuario já cadastrado")
    else:
        passwd_encrypted = bcrypt_context.hash(useschemas.passwd)
        new_user = User(useschema.name, useschema.email, passwd_encrypted, useschema.active, useschema.admin)   # Recebe os dados
        session.add(new_user) # adiciona os dados no banco de dados
        session.commit() # cria o commit para a modificação
        return {"mensagem": f"usuário cadastrado com sucesso! {useschema.email}"}

# LOGIN
@auth_router.post("/signin")
async def signin(signinschema: SignInSchema, session: Session = Depends(catch_session)):
    # verifica se dentro da tabela usuario tem o usuario inserido na rota
    user = session.query(User).filter(User.email == signinschema.email).first()
    if not user:
        raise HTTPException(status_code=400, detail="Usuario nao encontrado")
    else:
        acess_token = crate_token(user.id)
        return {
            "acess-token" : acess_token,
            "token_type" : "Bearer"
        }

        # JWT Bearer

        # header = {"Acess-Token" : "Bearer token"}