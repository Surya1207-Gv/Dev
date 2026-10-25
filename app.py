
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel):
    id: int
    name: str
    marks: float

students = {}

@app.post("/students")
def add(s: Student):
    if s.id in students:
        raise HTTPException(400, "Student already exists")
    students[s.id] = s
    return s

@app.get("/students")
def get_all():
    return students

@app.get("/students/{id}")
def get_one(id: int):
    if id not in students:
        raise HTTPException(404, "Student not found")
    return students[id]

@app.put("/students/{id}")
def update(id: int, s: Student):
    if id not in students:
        raise HTTPException(404, "Student not found")
    if id != s.id:
        raise HTTPException(400, "ID mismatch")
    students[id] = s
    return s

@app.delete("/students/{id}")
def delete(id: int):
    if id not in students:
        raise HTTPException(404, "Student not found")
    del students[id]
    return {"message": "Student deleted"}
