# ROTAS GLOBAIS
from fastapi import APIRouter

order_routes = APIRouter(prefix="/requests", tags=["requests"])

@order_routes.get("/")
async def home():
    return {"mensagem": "Você acessou sua rota de pedidos!"}