from fastapi import APIRouter, HTTPException

from app.models.todo_item import TodoItem

router = APIRouter()

# Create initial todo task
todo_items_list: list[TodoItem] = [
  TodoItem(
    id=1,
    title="Test Reminder App",
    description="Please Add and delete reminder tasks in order to test this Reminder App. Thank you!"
  )
]

# Get all todo items
@router.get("/tasks", status_code=200)
def get_tasks():
  return todo_items_list

# Get Todo Item by id
@router.get("/tasks/{id}", status_code=200)
def get_task(id):
  task: TodoItem | None = next(filter(lambda x: x.id == int(id), todo_items_list), None)

  if not task:
    raise HTTPException(status_code=404, detail="Task not found.")
  
  return {"task": task}

# Create a new todo item
@router.post("/tasks", status_code=201)
def create_task(item: TodoItem):
  if len(todo_items_list) > 0:
    max_id: int = max(todo_items_list, key=lambda y: y.id).id
  else:
    max_id = 0

  item.id = max_id + 1
  todo_items_list.append(item)

  return { "task": item }

# Delete an existing todo item
@router.delete("/tasks/{id}", status_code=204)
def delete_task(id: int) -> None:
  task: TodoItem | None = next(filter(lambda x: x.id == int(id), todo_items_list), None)

  if not task:
    raise HTTPException(status_code=404, detail="Task not found.")

  todo_items_list.remove(task)
  return