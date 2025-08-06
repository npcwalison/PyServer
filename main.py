from fastapi import FastAPI

app = FastAPI()

from apps.users.urls import auth_routes
from config.urls import order_router

app.include_router(auth_routes)
app.include_router(order_router)