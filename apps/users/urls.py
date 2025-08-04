# ROTAS ESPECIFICAS
from fastapi import APIRouter

auth_routes = APIRouter(prefix="/auth", tags=["auth"])

order_routes = APIRouter(prefix="/auth", tags=["auth"])

@order_routes.get("/")
async def home():
    return {"mensagem": "pagina de autenticação!"}