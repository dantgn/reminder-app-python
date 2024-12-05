from fastapi import FastAPI
from app.api import todo_item

def include_routers(app: FastAPI):
    app.include_router(todo_item.router, tags=["tasks"])

