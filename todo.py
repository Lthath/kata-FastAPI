from fastapi import FastAPI, HTTPException
from typing import Optional, List
from pydantic import BaseModel
from model import Todo 

app = FastAPI(title="Lthat TODO API", version="v1")


store_todo=[]


@app.get("/")
async def home():
  return {"Message": "Hello World"}

@app.get("/todos/", response_model=List[Todo])
async def get_all_todos():
  return store_todo

@app.get("/todo/{id}")
async def get_todo(id: int):
  try:
    return store_todo[id]
  except:
    raise HTTPException(status_code=404, detail="Todo not found in DB")

@app.post("/todo")
async def create_todo(todo: Todo):
  store_todo.append(todo)
  return todo 

@app.put("/todo/{id}")
async def update_todo(id: int, new_todo: Todo):
  try:
    store_todo[id] = new_todo
    return store_todo[id]
  except: 
    raise HTTPException(status_code=404, detail="Todo not found in DB")
  

@app.delete("/todo/{id}")
async def delete_todo(id: int):
  try:
    obj = store_todo[id]
    store_todo.pop(id)
    return obj
  except:
    raise HTTPException(status_code=404, detail="Todo not found in DB")

    