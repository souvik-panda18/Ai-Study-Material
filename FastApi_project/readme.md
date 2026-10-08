# FastAPI Learning & CRUD API

A hands-on FastAPI learning project built to understand the fundamentals of building REST APIs with Python. This project started from basic FastAPI routes and gradually evolved into a structured CRUD API with Pydantic validation, query/path parameters, dependency injection, response models, HTTP status codes, and `APIRouter`.

---

## 📌 Project Overview

The goal of this project was to learn FastAPI **step-by-step by building an actual API**, rather than only studying the theory.

The final project is an **LLM Model Management API** that allows users to:

- View all AI models
- Search/filter models
- Get a model by ID
- Create a new model
- Update a model
- Delete a model
- Validate incoming data
- Handle API errors properly
- Explore the API through Swagger UI

---

# 🛠️ Tech Stack

- **Python**
- **FastAPI**
- **Pydantic**
- **Uvicorn**
- **Swagger / OpenAPI**
- In-memory Python data structure (current version)

### Planned

- SQLAlchemy
- SQLite / PostgreSQL
- Authentication
- JWT
- Testing
- Deployment

---

# 📚 What I Learned

## 1. FastAPI Fundamentals

Learned how to create a basic FastAPI application.

```python
from fastapi import FastAPI

app = FastAPI()
```

Created basic routes using decorators:

```python
@app.get("/")
def root():
    return {"message": "Hello World"}
```

### Key concepts

- FastAPI application
- Routes
- Endpoints
- HTTP requests
- HTTP responses
- JSON responses
- Uvicorn server
- Auto-generated API documentation

---

# 2. Running a FastAPI Application

Learned how to run the application using Uvicorn:

```bash
uvicorn main:app --reload
```

Understanding:

```text
uvicorn → ASGI server
main    → main.py
app     → FastAPI application object
--reload → automatically reload during development
```

---

# 3. Swagger / OpenAPI Documentation

FastAPI automatically generates interactive API documentation.

```text
http://127.0.0.1:8000/docs
```

Using Swagger UI, I learned how to:

- View available endpoints
- See HTTP methods
- Provide parameters
- Send request bodies
- Execute API requests
- Inspect responses
- Test validation errors

---

# 4. HTTP Methods

Learned the main HTTP methods used in REST APIs.

| Method | Purpose |
|---|---|
| GET | Read data |
| POST | Create data |
| PUT | Update data |
| DELETE | Delete data |

Implemented:

```text
GET     /models
GET     /models/{model_id}
POST    /models
PUT     /models/{model_id}
DELETE  /models/{model_id}
```

---

# 5. CRUD Operations

Learned the CRUD pattern:

```text
Create → POST
Read   → GET
Update → PUT
Delete → DELETE
```

Implemented a complete CRUD API for AI models.

Example model:

```json
{
    "id": 1,
    "name": "Llama 3",
    "provider": "Meta"
}
```

---

# 6. Path Parameters

Learned how to use dynamic values inside URLs.

Example:

```python
@app.get("/models/{model_id}")
def get_model(model_id: int):
    ...
```

Request:

```text
GET /models/2
```

FastAPI automatically provides:

```python
model_id = 2
```

Also learned type validation:

```python
model_id: int
```

---

# 7. Query Parameters

Learned how to use query parameters for filtering and controlling API responses.

Example:

```text
/models?provider=OpenAI
```

Implemented filtering:

```python
@app.get("/models")
def get_models(provider: str = None):
    ...
```

Also implemented a `limit` parameter:

```python
limit: int = Query(
    default=10,
    ge=1,
    le=100
)
```

Example:

```text
/models/search?provider=OpenAI&limit=5
```

This introduced the idea of **pagination and result limiting**.

---

# 8. Pydantic Models

Learned how FastAPI uses Pydantic for request validation.

Example:

```python
class Model(BaseModel):
    id: int
    name: str
    provider: str
```

FastAPI automatically validates incoming JSON against the model.

Example:

```json
{
    "id": 1,
    "name": "GPT-4o",
    "provider": "OpenAI"
}
```

---

# 9. Separate Create Models

Learned that the data required to create a resource can be different from the data returned by the API.

Created:

```python
class ModelCreate(BaseModel):
    name: str
    provider: str
```

Instead of requiring the client to send an ID, the server generates it.

Request:

```json
{
    "name": "Claude",
    "provider": "Anthropic"
}
```

Server generates:

```text
id = 3
```

This is a more realistic API design.

---

# 10. Pydantic Field Validation

Learned how to add constraints using `Field`.

```python
class ModelCreate(BaseModel):
    name: str = Field(
        ...,
        min_length=1,
        max_length=100
    )

    provider: str = Field(
        ...,
        min_length=1,
        max_length=100
    )
```

This allows the API to automatically reject invalid input.

---

# 11. Response Models

Learned how to control and validate API responses.

Example:

```python
@app.get(
    "/models",
    response_model=list[Model]
)
def get_models():
    ...
```

And:

```python
@app.get(
    "/models/{model_id}",
    response_model=Model
)
def get_model(model_id: int):
    ...
```

Response models help ensure that the API returns the expected structure.

---

# 12. HTTP Status Codes

Learned the purpose of common HTTP status codes.

| Status Code | Meaning |
|---|---|
| 200 | Success |
| 201 | Resource created |
| 204 | Success with no content |
| 400 | Bad request |
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Resource not found |
| 422 | Validation error |
| 500 | Server error |

Implemented `201 Created` for POST:

```python
@app.post(
    "/models",
    response_model=Model,
    status_code=status.HTTP_201_CREATED
)
```

---

# 13. HTTPException

Learned how to return proper HTTP errors.

Instead of:

```python
return {"error": "Model not found"}
```

implemented:

```python
raise HTTPException(
    status_code=404,
    detail="Model not found"
)
```

This allows the API to return an actual:

```text
404 Not Found
```

---

# 14. Dependency Injection

Learned FastAPI's `Depends()` system.

Example:

```python
from fastapi import Depends

def get_api_info():
    return {
        "name": "LLM Model API",
        "version": "1.0"
    }


@app.get("/info")
def api_info(info=Depends(get_api_info)):
    return info
```

Understanding:

```text
Request
   ↓
Depends()
   ↓
Dependency function
   ↓
Result
   ↓
Endpoint
```

This concept will become especially important when working with:

- Database sessions
- Authentication
- Authorization
- Current users
- API keys
- Shared services

---

# 15. APIRouter

Learned how to separate API routes into different modules.

Instead of putting everything inside `main.py`, the project now uses:

```text
fastapi_project/
│
├── main.py
│
└── routers/
    └── models.py
```

Created a router:

```python
router = APIRouter(
    prefix="/models",
    tags=["Models"]
)
```

Then connected it to the main application:

```python
app.include_router(models_router)
```

This makes the application easier to maintain and scale.

---

# 📂 Current Project Structure

```text
fastapi_project/
│
├── main.py
│
└── routers/
    └── models.py
```

### `main.py`

Responsible for:

- Creating the FastAPI application
- Root endpoint
- API-level dependencies
- Including routers

### `routers/models.py`

Responsible for:

- Model Pydantic schemas
- Model CRUD operations
- Model routes
- Model validation
- Model-related errors

---

# 🔄 Request Flow

The concepts learned can be summarized as:

```text
Client
  │
  │ HTTP Request
  ▼
FastAPI Route
  │
  ├── Path Parameters
  ├── Query Parameters
  ├── Request Body
  │
  ▼
Pydantic Validation
  │
  ▼
Dependency Injection
  │
  ▼
Business Logic
  │
  ▼
Database / Data Source
  │
  ▼
Response Model
  │
  ▼
HTTP Status Code
  │
  ▼
JSON Response
```

---

# 🧪 Current API Endpoints

## Root

```http
GET /
```

Response:

```json
{
    "message": "Welcome to LLM Model API"
}
```

---

## Get All Models

```http
GET /models/
```

---

## Filter Models

```http
GET /models/?provider=OpenAI
```

---

## Search Models

```http
GET /models/search?provider=OpenAI&limit=10
```

---

## Get Model by ID

```http
GET /models/1
```

---

## Create Model

```http
POST /models/
```

Request:

```json
{
    "name": "Claude",
    "provider": "Anthropic"
}
```

---

## Update Model

```http
PUT /models/1
```

---

## Delete Model

```http
DELETE /models/1
```

---

## API Information

```http
GET /info
```

---

# ▶️ How to Run

## 1. Clone the repository

```bash
git clone <your-repository-url>
cd fastapi_project
```

## 2. Create virtual environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

## 3. Install dependencies

```bash
pip install fastapi uvicorn pydantic
```

## 4. Start the server

```bash
uvicorn main:app --reload
```

## 5. Open API documentation

```text
http://127.0.0.1:8000/docs
```

---

# 🧠 Learning Progression

The learning path followed was:

```text
1. FastAPI Basics
       ↓
2. Routes & Endpoints
       ↓
3. HTTP Methods
       ↓
4. CRUD
       ↓
5. Path Parameters
       ↓
6. Query Parameters
       ↓
7. Request Bodies
       ↓
8. Pydantic Models
       ↓
9. Validation
       ↓
10. Response Models
       ↓
11. HTTP Status Codes
       ↓
12. HTTPException
       ↓
13. Dependency Injection
       ↓
14. APIRouter
       ↓
15. Modular Project Structure
```

---

# 🚧 Next Learning Steps

This project currently uses an **in-memory Python list** as its database.

The next stage will replace it with a real database.

### Phase 2 — Database

- SQLAlchemy
- SQLite
- Database models
- Sessions
- Database dependencies
- CRUD with SQLAlchemy
- Relationships
- PostgreSQL

### Phase 3 — Authentication

- Password hashing
- OAuth2
- JWT
- Authentication dependencies
- Protected routes
- Authorization

### Phase 4 — Production FastAPI

- Async programming
- Middleware
- CORS
- Environment variables
- `.env`
- Exception handlers
- Logging
- Testing
- Deployment

### Phase 5 — AI Integration

Eventually this FastAPI knowledge will be used for:

```text
FastAPI
   │
   ├── LLM APIs
   ├── RAG
   ├── Embeddings
   ├── Vector Databases
   ├── AI Agents
   └── MCP
```

---

# 🎯 Learning Goal

The purpose of this project is not just to create a CRUD API, but to build a strong backend foundation for future **AI/ML applications**.

The next major milestone is:

```text
FastAPI
   ↓
SQLAlchemy + Database
   ↓
Authentication
   ↓
LLM API Integration
   ↓
RAG
   ↓
AI Agents
```

---

## Current Status

**FastAPI Fundamentals: Completed ✅**

**CRUD API: Completed ✅**

**Pydantic Validation: Completed ✅**

**Dependency Injection: Completed ✅**

**APIRouter / Modular Structure: Completed ✅**

**Database Integration: Next 🔜**