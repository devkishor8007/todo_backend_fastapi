from fastapi import APIRouter, HTTPException
from apps.models.todo import TodoModel
from apps.schemas.todo import todosEntity, todoEntity
from bson import ObjectId
from apps.services.todo import Todo

todo = Todo()

router = APIRouter(
    prefix="/api/v1"
)

@router.get('/')
def get_root():
    return "Hello"

@router.get("/todos", tags=["todo"])
async def get_todos(title: str | None = None, limit: int = 7, page: int = 1):
    query = {}
    page_size = limit
    page_number = page

    if page_number < 1:
        page_number = 1

    skip = (page_number - 1) * page_size

    if title:
        query["title"] = title

    todod  = todosEntity(todo.find_all(query).sort({"created_at": -1}).skip(skip).limit(page_size))
    return todod

@router.get("/todos/{id}", tags=["todo"])
async def get_todo(id: str):
    result = todoEntity(todo.find_one({"_id": ObjectId(id)}))
    if result:
        return result
    else:
        raise HTTPException(status_code=404, detail="Todo not found")

@router.post("/todos", tags=["todo"], status_code=201)
async def create_todo(inputTodo: TodoModel):
    todo.create(inputTodo)
    return {"message": "Todo created successfully"}

@router.patch("/todos/{id}", tags=["todo"], status_code=200)
async def update_todo(id: str, inputTodo: TodoModel):
    todo.update_todo(ObjectId(id), inputTodo)
    return {"message": "Todo updated successfully"}

@router.delete("/todos/{id}", tags=["todo"], status_code=200)
async def remove_todo(id: str):
    todoEntity(todo.delete_one({"_id": ObjectId(id)}))
    return { "success": True, "message": "delete todo successfully" }