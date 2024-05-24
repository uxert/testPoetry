from typing import Union

from fastapi import FastAPI
from src.todo.router import todo_router
app = FastAPI()
app.include_router(todo_router, prefix="/todo")


@app.get("/")
def read_root():
    return {"Hello": "World2"}


@app.get("/health")
def check_health():
    return "ok"



