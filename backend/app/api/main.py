from fastapi import APIRouter
from .routes import home

api_router = APIRouter()
api_router.include_router(home.router)
