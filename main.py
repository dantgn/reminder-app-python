from fastapi import FastAPI, HTTPException
from models import TodoItem
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(root_path="/api",
            title="Reminder App",
            version="1.0.0")

# Create initial todo task
todo_items_list: list[TodoItem] = [
  TodoItem(
    id=1,
    title="Test Reminder App",
    description="Please Add and delete reminder tasks as you please in order to test this Reminder App. Thank you."
  )
]

@app.get("/")
def root():
    return {"message": "Hello World"}

# Route to get all todo_items
@app.get("/tasks", status_code=200)
def get_tasks():
  return todo_items_list

# Route to get todo item by id
@app.get("/tasks/{id}", status_code=200)
def get_task(id):
  task: TodoItem | None = next(filter(lambda x: x.id == int(id), todo_items_list), None)

  if not task:
    raise HTTPException(status_code=404, detail="Task not found.")
  
  return {"task": task}


@app.post("/tasks", status_code=201)
def create_task(item: TodoItem):
  if len(todo_items_list) > 0:
    max_id: int = max(todo_items_list, key=lambda y: y.id).id
  else:
    max_id = 0

  item.id = max_id + 1
  todo_items_list.append(item)

  return { "task": item }

@app.delete("/tasks/{id}", status_code=204)
def delete_task(id: int) -> None:
  task: TodoItem | None = next(filter(lambda x: x.id == int(id), todo_items_list), None)

  if not task:
    raise HTTPException(status_code=404, detail="Task not found.")

  todo_items_list.remove(task)
  return

origins: list[str] = [
    "http://localhost",
    "http://localhost:5173",
    "https://reminder-tasks-frontend.vercel.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=(origins),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
