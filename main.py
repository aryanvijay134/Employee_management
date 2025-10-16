from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import db  

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/employees")
def list_employees():
    return db.get_employees()

@app.get("/departments")
def list_departments():
    return db.get_departments()

@app.get("/")   
def home():
    return {"message": "🚀 API is running! Go to /employees or /departments"}

