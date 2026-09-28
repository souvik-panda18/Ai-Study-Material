from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Model(BaseModel):
    id: int
    name: str
    provider: str


# Dummy in-memory database
db_models = [
    {"id": 1, "name": "Llama 3", "provider": "Meta"},
    {"id": 2, "name": "GPT-4o", "provider": "OpenAI"},
]
# ("/")this creates route 
@app.get("/")
def root():
    return {"message": "Welcome to LLM Model API"}

@app.get("/models")
def get_all_models():
    return db_models
# to run this in terminal use command uvicorn main:app --reload
# paremetized route to post model by id
@app.get("/models/{model_id}")
def get_model_by_id(model_id: int):
    for model in db_models:
        if model["id"] == model_id:
            return model
    return {"error": "Model not found"}