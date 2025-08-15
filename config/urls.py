# ROTAS GLOBAIS
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from apps.users.schemas import  RequestSchema
from core.utils import catch_session
from core.models import Request

order_router = APIRouter(prefix="/requests", tags=["requests"])

@order_router.get("/")
async def home():
    return {"mensagem": "Você acessou sua rota de pedidos!"}


# criar pedidos
@order_router.post("/request")
async def create_request(requestschema: RequestSchema, session: Session = Depends(catch_session)):
    new_request = Request(user = requestschema.user)
    session.add(new_request)
    session.commit()
    return {"mensage": f"Pedido criado com sucesso: {new_request.id}"}