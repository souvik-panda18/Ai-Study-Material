REST APIs + HTTP

Spend about 2 hours on this.

1. HTTP basics — 20 min

Understand:

Client → Request → Server
Client ← Response ← Server

Learn:

HTTP
URL
Endpoint
Request
Response
HTTP methods
GET
POST
PUT
PATCH
DELETE
Status codes
200
201
400
404
500
HTTP (Hypertext Transfer Protocol) is the foundational protocol used for transmitting data across the web between a **Client** (e.g., your browser or a Python script) and a **Server** (where the website or API hosted).

---

### Core Concepts

* **Client & Server Relationship:**
* **Client:** Sends an HTTP Request asking for data or an action.
* **Server:** Processes the request and returns an HTTP Response containing status details and data.


* **URL (Uniform Resource Locator):** The address used to access web resources (e.g., `[https://api.github.com/users](https://api.github.com/users)`).
* **Endpoint:** A specific path on the server that handles a specific function or resource (e.g., `/users` or `/models`).

---

### Key HTTP Methods (CRUD Operations)

HTTP methods tell the server what action to perform on a resource:

| Method | Description | CRUD Equivalent |
| --- | --- | --- |
| **GET** | Retrieves data from the server without modifying anything. | Read |
| **POST** | Sends new data to the server to create a resource. | Create |
| **PUT** | Replaces an entire existing resource with new data. | Update |
| **PATCH** | Partially updates an existing resource. | Update |
| **DELETE** | Removes a resource from the server. | Delete |

---

### Common HTTP Status Codes

Status codes tell you the outcome of an HTTP request:

* **2xx (Success):**
* `200 OK`: Request succeeded.
* `201 Created`: Resource was successfully created (common with `POST`).


* **4xx (Client Errors):**
* `400 Bad Request`: Server couldn't understand the request (invalid syntax/payload).
* `401 Unauthorized` / `403 Forbidden`: Authentication or permission missing.
* `404 Not Found`: The requested URL/endpoint does not exist.


* **5xx (Server Errors):**
* `500 Internal Server Error`: The server encountered an unexpected error.



---

### Quick Python Example (`requests`)

```python
import requests

# GET Request
response = requests.get("https://api.github.com")
print(response.status_code)  # 200
print(response.json())         # Parsed JSON response

# POST Request
data = {"name": "Llama", "provider": "Meta"}
response = requests.post("https://example.com/api/models", json=data)

```
2. Python requests — 30 min

Install:

pip install requests

Learn:

import requests

response = requests.get("https://api.github.com")

print(response.status_code)
print(response.text)

Then JSON:

data = response.json()

print(data)

Understand the difference between:

response.text

and:

response.json()
3. GET requests — 20 min

Practice calling a public API.

Learn:

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)

Also learn:

params = {
    "page": 1,
    "limit": 10
}

response = requests.get(url, params=params)
4. POST requests — 20 min

Learn how Python sends JSON to an API:

data = {
    "name": "Llama",
    "provider": "Meta",
    "temperature": 0.7
}

response = requests.post(
    url,
    json=data
)

print(response.status_code)
print(response.json())

This is particularly important for your future FastAPI + AI projects.

5. Error handling — 10 min

Combine APIs with your exception-handling knowledge:

try:
    response = requests.get(url, timeout=5)
    response.raise_for_status()

    data = response.json()

except requests.RequestException as e:
    print("API request failed:", e)
🧪 Mini Project

After learning the basics, build:

LLM API Client

You'll make a Python program like:

===== LLM API Client =====

1. Get models
2. Get model details
3. Create model
4. Delete model
5. Exit

The important part is that this time your program won't store everything locally.

You'll have:

Python Client
      ↓
HTTP Request
      ↓
REST API
      ↓
JSON Response
      ↓
Python

And this sets you up for the next major step: