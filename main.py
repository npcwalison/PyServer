from fastapi import FastAPI

app = FastAPI()

from apps.users.urls import auth_router
# from config.urls import order_router

app.include_router(auth_router)
# app.include_router(order_router)