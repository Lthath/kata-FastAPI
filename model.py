from pydantic import BaseModel

class Todo(BaseModel):
  
  name: str
  due_date: str
  description: str
  