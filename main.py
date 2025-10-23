from fastapi import FastAPI, Depends
from database import initialize_db, get_conn
from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    age: int

class UserOut(BaseModel):
    id: int
    name: str
    age: int

def get_db():
    conn = get_conn()
    try:
        yield conn
    finally:
        conn.close()

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    initialize_db()

@app.post("/users/", response_model=UserOut)
def add_user(user: UserCreate, conn = Depends(get_db)):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, age) VALUES (%s, %s)", (user.name, user.age))
    conn.commit()
    user_id = cursor.lastrowid
    cursor.close()
    return {"id": user_id, "name": user.name, "age": user.age}
