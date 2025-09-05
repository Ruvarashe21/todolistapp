# backend/routes/todo_routes.py
# backend/routes/todo_routes.py
from fastapi import APIRouter, Depends, HTTPException, Header
from sqlalchemy.orm import Session
from backend.database import SessionLocal
from backend.models import Todo, User
from backend.schema import TodoCreate, TodoUpdate
from backend.auth import validate_token

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(token: str, db: Session):
    email = validate_token(token)
    if email in ["Token has expired", "Invalid token"]:
        raise HTTPException(status_code=401, detail=email)
    user = db.query(User).filter(User.email == email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.get("/todos")
def get_todos(authorization: str = Header(None), db: Session = Depends(get_db)):
    token = authorization.split(" ")[1] if authorization else None
    user = get_current_user(token, db)
    todos = db.query(Todo).filter(Todo.user_id == user.id).all()
    return todos

@router.post("/todos")
def create_todo(todo: TodoCreate, authorization: str = Header(None), db: Session = Depends(get_db)):
    token = authorization.split(" ")[1] if authorization else None
    user = get_current_user(token, db)
    new_todo = Todo(text=todo.text, user_id=user.id)
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo

@router.put("/todos/{todo_id}")
def update_todo(todo_id: int, todo: TodoUpdate, authorization: str = Header(None), db: Session = Depends(get_db)):
    token = authorization.split(" ")[1] if authorization else None
    user = get_current_user(token, db)
    existing = db.query(Todo).filter(Todo.id == todo_id, Todo.user_id == user.id).first()
    if not existing:
        raise HTTPException(status_code=404, detail="Todo not found")
    existing.text = todo.text
    existing.completed = todo.completed
    db.commit()
    return existing

@router.delete("/todos/{todo_id}")
def delete_todo(todo_id: int, authorization: str = Header(None), db: Session = Depends(get_db)):
    token = authorization.split(" ")[1] if authorization else None
    user = get_current_user(token, db)
    todo = db.query(Todo).filter(Todo.id == todo_id, Todo.user_id == user.id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    db.delete(todo)
    db.commit()
    return {"message": "Todo deleted"}