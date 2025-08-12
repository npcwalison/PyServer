# ROTAS GLOBAIS
from fastapi import APIRouter

order_router = APIRouter(prefix="/requests", tags=["requests"])

@order_router.get("/")
async def home():
    return {"mensagem": "Você acessou sua rota de pedidos!"}