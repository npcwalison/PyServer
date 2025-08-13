from fastapi import FastAPI
from passlib.context import CryptContext
from dotenv import load_dotenv
import os

load_dotenv() # carrega as variaveis de ambiente

SECRET_KEY = os.getenv("SECRET_KEY")

app = FastAPI()

# deprecated, descarta criptografia obsoleta.
bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

from apps.users.urls import auth_router
from config.urls import order_router

app.include_router(auth_router)
app.include_router(order_router)