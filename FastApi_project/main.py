from fastapi import FastAPI, Depends

from routers.models import router as models_router


app = FastAPI()


# -----------------------------
# Dependency
# -----------------------------

def get_api_info():
    return {
        "name": "LLM Model API",
        "version": "1.0"
    }


# -----------------------------
# Root Route
# -----------------------------

@app.get("/")
def root():
    return {"message": "Welcome to LLM Model API"}


# -----------------------------
# API Info - Dependency Injection
# -----------------------------

@app.get("/info")
def api_info(info=Depends(get_api_info)):
    return info


# -----------------------------
# Include Model Router
# -----------------------------

app.include_router(models_router)
