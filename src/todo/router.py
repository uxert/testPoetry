

from fastapi import APIRouter

todo_list = [
    {
        "id": 1,
        "name": "Nazwa zadania",
        "assignee": "osoba",
        "done": True
    },
    {
        "id": 2,
        "name": "Zadanie 2",
        "assignee": "osoba2",
        "done": False
    }
]

todo_router = APIRouter()


@todo_router.get("/")
def get_all():
    return todo_list


@todo_router.get("/{item_id}")
def get_one(item_id: int):

    return [
        [item for item in todo_list if item["id"] == item_id]
    ][0]


