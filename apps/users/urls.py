# ROTAS ESPECIFICAS
from fastapi import APIRouter

auth_router = APIRouter(prefix="/auth", tags=["auth"])

#ROTA PRINCIPAL
@auth_router.get("/")
async def home():
    return {"mensagem": "pagina de autenticação!"}


# CRIAR USUARIO
@auth_router.post("/signup")
async def signup(email: str, senha: str):
    return