# Module 1: Introduction to FastAPI

## Table of Contents
1. [What is FastAPI?](#1-what-is-fastapi)
2. [Setting up your development environment](#2-setting-up-your-development-environment)
3. [Your first FastAPI application](#3-your-first-fastapi-application)
4. [Understanding automatic API documentation](#4-understanding-automatic-api-documentation)

---

## 1. What is FastAPI?

### Overview
FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints. 

### Key Features

#### 🚀 Fast Performance
- One of the fastest Python frameworks available
- Comparable to NodeJS and Go
- Built on Starlette and Pydantic

#### 💡 Easy to Use
- Intuitive and easy to learn
- Less time reading documentation
- Designed to be easy to use and learn

#### 🔧 Automatic Documentation
- Automatically generates interactive API documentation
- Swagger UI and ReDoc included out of the box
- No additional configuration needed

#### ✅ Type Hints & Validation
- Uses Python type hints for parameter declaration
- Automatic data validation
- Better IDE support with autocomplete

#### 🎯 Production Ready
- Ready for production use
- Automatic data serialization
- Built-in security features

### Why Choose FastAPI?

| Feature | FastAPI | Flask | Django |
|---------|---------|-------|--------|
| Performance | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| Async Support | ✅ Native | ⚠️ Limited | ⚠️ Limited |
| Auto Documentation | ✅ Built-in | ❌ Manual | ❌ Manual |
| Type Hints | ✅ Required | ⚠️ Optional | ⚠️ Optional |
| Learning Curve | Easy | Easy | Moderate |
| Best For | APIs | Web Apps | Full Stack |

### Real-World Use Cases
- RESTful APIs
- Microservices architecture
- Machine Learning model deployment
- IoT backend systems
- Real-time applications with WebSockets
- High-performance data processing APIs

---

## 2. Setting up your development environment

### Prerequisites

Before you begin, ensure you have:
- **Python 3.7+** installed on your system
- **pip** (Python package manager)
- A code editor (VS Code, PyCharm, or any text editor)
- Basic knowledge of Python

### Step 1: Check Python Version

```bash
python --version
# or
python3 --version
```

Expected output: `Python 3.7.0` or higher

### Step 2: Create Project Directory

```bash
# Create a new directory for your project
mkdir fastapi-tutorial
cd fastapi-tutorial
```

### Step 3: Create Virtual Environment

A virtual environment isolates your project dependencies from other Python projects. 

**On Windows:**
```bash
python -m venv venv
```

**On macOS/Linux:**
```bash
python3 -m venv venv
```

### Step 4: Activate Virtual Environment

**On Windows:**
```bash
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
source venv/bin/activate
```

You should see `(venv)` at the beginning of your command prompt. 

### Step 5: Install FastAPI and Dependencies

```bash
# Install FastAPI
pip install fastapi

# Install ASGI server (Uvicorn)
pip install "uvicorn[standard]"
```

### Step 6: Verify Installation

```bash
pip list
```

You should see `fastapi` and `uvicorn` in the list.

### Step 7: Create Requirements File

```bash
pip freeze > requirements.txt
```

**requirements.txt** content should look like:
```
annotated-types==0.6.0
anyio==4.2.0
click==8.1.7
fastapi==0.109.0
h11==0.14. 0
httptools==0.6.1
idna==3.6
pydantic==2.5.3
pydantic_core==2.14.6
python-dotenv==1.0.0
PyYAML==6.0. 1
sniffio==1.3.0
starlette==0.35.1
typing_extensions==4.9.0
uvicorn==0.27.0
uvloop==0.19.0
watchfiles==0.21.0
websockets==12.0
```

### IDE Setup (Optional but Recommended)

#### VS Code Extensions
- Python
- Pylance
- Python Test Explorer
- Thunder Client (for API testing)

#### PyCharm
- Built-in Python support
- HTTP Client for API testing

### Troubleshooting

**Problem:** `python` command not found
- **Solution:** Use `python3` instead or add Python to PATH

**Problem:** Permission denied when installing packages
- **Solution:** Make sure virtual environment is activated

**Problem:** Virtual environment activation not working
- **Solution (Windows):** Run `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` in PowerShell

---

## 3. Your first FastAPI application

### Creating a Basic FastAPI App

Create a new file called `main.py`:

```python
# main.py
from fastapi import FastAPI

# Create an instance of FastAPI
app = FastAPI()

# Define a route
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}
```

### Running the Application

```bash
uvicorn main:app --reload
```

**Command Breakdown:**
- `uvicorn`: ASGI server
- `main`: the file name (main.py)
- `app`: the FastAPI instance name
- `--reload`: auto-restart server on code changes (development only)

### Expected Output

```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [28720]
INFO:     Started server process [28722]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

### Testing Your API

Open your browser and visit: `http://127.0.0.1:8000`

You should see:
```json
{
  "message": "Hello, World!"
}
```

### Adding More Routes

Let's expand our application:

```python
# main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/about")
def about():
    return {
        "app_name": "FastAPI Tutorial",
        "version": "1. 0.0",
        "author": "Your Name"
    }

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

@app.get("/users/{user_id}")
def read_user(user_id: int, query: str = None):
    return {"user_id": user_id, "query": query}
```

### Understanding the Code

#### 1. Import FastAPI
```python
from fastapi import FastAPI
```

#### 2. Create an Instance
```python
app = FastAPI()
```
This creates your application instance.

#### 3. Define Routes (Endpoints)
```python
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}
```

- `@app.get("/")`: Decorator that defines a GET endpoint at root path
- `def read_root()`: Function that handles the request
- `return {... }`: Response data (automatically converted to JSON)

#### 4.  Path Parameters
```python
@app. get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}
```

- `{item_id}`: Path parameter
- `item_id: int`: Type hint for automatic validation

#### 5. Query Parameters
```python
@app.get("/users/{user_id}")
def read_user(user_id: int, query: str = None):
    return {"user_id": user_id, "query": query}
```

- `query: str = None`: Optional query parameter
- Access via: `http://127.0.0.1:8000/users/1?query=test`

### HTTP Methods

FastAPI supports all HTTP methods:

```python
@app.get("/")      # GET request
@app.post("/")     # POST request
@app.put("/")      # PUT request
@app.delete("/")   # DELETE request
@app.patch("/")    # PATCH request
@app.options("/")  # OPTIONS request
@app.head("/")     # HEAD request
```

### Practice Exercise

Create an endpoint that:
1.  Accepts a name as a path parameter
2.  Accepts an optional age as a query parameter
3. Returns a greeting message

**Solution:**
```python
@app. get("/greet/{name}")
def greet_user(name: str, age: int = None):
    if age:
        return {"message": f"Hello, {name}! You are {age} years old."}
    return {"message": f"Hello, {name}!"}
```

Test it:
- `http://127.0.0.1:8000/greet/John`
- `http://127. 0.0.1:8000/greet/John?age=25`

---

## 4. Understanding automatic API documentation

### What is API Documentation?

API documentation describes:
- Available endpoints
- Required parameters
- Response formats
- Example requests and responses
- Data types and validation rules

### FastAPI's Built-in Documentation

FastAPI automatically generates **interactive API documentation** using:
1. **Swagger UI** - Interactive testing interface
2. **ReDoc** - Clean, readable documentation

### Accessing Swagger UI

Start your server:
```bash
uvicorn main:app --reload
```

Visit: **http://127.0.0. 1:8000/docs**

#### Features of Swagger UI:
- ✅ List of all endpoints
- ✅ Try out endpoints directly in browser
- ✅ See request/response formats
- ✅ View data models
- ✅ Authentication testing

### Accessing ReDoc

Visit: **http://127.0. 0.1:8000/redoc**

#### Features of ReDoc:
- ✅ Clean, professional layout
- ✅ Better for sharing with stakeholders
- ✅ Three-panel design
- ✅ Responsive design
- ✅ Print-friendly

### Enhancing Documentation

#### Adding Metadata

```python
from fastapi import FastAPI

app = FastAPI(
    title="My FastAPI Tutorial",
    description="A comprehensive FastAPI learning project",
    version="1.0.0",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Your Name",
        "url": "http://example.com/contact/",
        "email": "your.email@example.com",
    },
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT",
    },
)
```

#### Adding Endpoint Descriptions

```python
@app.get(
    "/items/{item_id}",
    summary="Get an item",
    description="Retrieve an item by its unique ID",
    response_description="The requested item",
)
def read_item(item_id: int):
    """
    Retrieve an item with the following information:
    
    - **item_id**: The unique identifier of the item
    """
    return {"item_id": item_id}
```

#### Adding Tags for Organization

```python
@app.get("/users/", tags=["users"])
def read_users():
    return [{"username": "user1"}, {"username": "user2"}]

@app.get("/items/", tags=["items"])
def read_items():
    return [{"name": "item1"}, {"name": "item2"}]

@app.post("/items/", tags=["items"])
def create_item():
    return {"message": "Item created"}
```

Tags group related endpoints together in the documentation.

#### Deprecating Endpoints

```python
@app. get("/old-endpoint/", deprecated=True)
def old_endpoint():
    return {"message": "This endpoint is deprecated"}
```

### Complete Example with Enhanced Documentation

```python
from fastapi import FastAPI
from typing import Optional

app = FastAPI(
    title="FastAPI Tutorial API",
    description="Learning FastAPI from scratch",
    version="1. 0.0",
)

@app.get(
    "/",
    tags=["general"],
    summary="Root endpoint",
    response_description="Welcome message",
)
def read_root():
    """
    # Welcome Endpoint
    
    Returns a simple welcome message. 
    
    This is the main entry point of the API.
    """
    return {"message": "Welcome to FastAPI Tutorial!"}

@app.get(
    "/items/{item_id}",
    tags=["items"],
    summary="Get item by ID",
)
def read_item(
    item_id: int,
    q: Optional[str] = None
):
    """
    Retrieve an item by its ID.
    
    - **item_id**: Required.  The ID of the item to retrieve
    - **q**: Optional. A query string for filtering
    """
    return {"item_id": item_id, "q": q}

@app.get(
    "/users/",
    tags=["users"],
    summary="List all users",
)
def list_users():
    """Get a list of all users in the system."""
    return [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"}
    ]
```

### OpenAPI Schema

FastAPI generates an OpenAPI schema automatically. 

Access it at: **http://127. 0.0.1:8000/openapi. json**

This JSON file contains:
- All endpoints
- Data models
- Validation rules
- Response types

You can use this schema with other tools like Postman, Insomnia, or code generators.

### Customizing Documentation URLs

```python
app = FastAPI(
    docs_url="/documentation",  # Default: /docs
    redoc_url="/redocumentation",  # Default: /redoc
    openapi_url="/api/v1/openapi.json"  # Default: /openapi. json
)
```

### Disabling Documentation (Production)

```python
app = FastAPI(
    docs_url=None,  # Disable Swagger UI
    redoc_url=None,  # Disable ReDoc
)
```

⚠️ Only disable in production if necessary for security reasons.

---

## 📝 Module 1 Summary

### What You Learned

✅ **FastAPI Basics**
- What FastAPI is and why it's powerful
- Key features and advantages over other frameworks

✅ **Development Environment**
- Installing Python and pip
- Creating virtual environments
- Installing FastAPI and Uvicorn

✅ **First Application**
- Creating a basic FastAPI app
- Defining routes and endpoints
- Path and query parameters
- Running the development server

✅ **API Documentation**
- Accessing Swagger UI and ReDoc
- Enhancing documentation with metadata
- Organizing endpoints with tags
- Understanding OpenAPI schema

### Key Concepts

| Concept | Description |
|---------|-------------|
| **FastAPI Instance** | `app = FastAPI()` - Your application object |
| **Route Decorator** | `@app.get("/")` - Defines an endpoint |
| **Path Parameter** | `/items/{item_id}` - Variable in URL |
| **Query Parameter** | `? name=value` - Optional URL parameters |
| **Type Hints** | `item_id: int` - Automatic validation |
| **Uvicorn** | ASGI server to run FastAPI |
| **Swagger UI** | Interactive API documentation |

### Commands Reference

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment (Windows)
venv\Scripts\activate

# Activate virtual environment (macOS/Linux)
source venv/bin/activate

# Install FastAPI
pip install fastapi

# Install Uvicorn
pip install "uvicorn[standard]"

# Run application
uvicorn main:app --reload

# Save dependencies
pip freeze > requirements.txt

# Install from requirements
pip install -r requirements.txt
```
### Common Errors & Solutions

#### Error 1: ModuleNotFoundError: No module named 'fastapi'
**Solution:** Install FastAPI: `pip install fastapi`

#### Error 2: Port already in use
**Solution:** Use a different port: `uvicorn main:app --reload --port 8001`

#### Error 3: 404 Not Found
**Solution:** Check your route definition and URL spelling

#### Error 4: Virtual environment not activated
**Solution:** Activate it: `source venv/bin/activate` or `venv\Scripts\activate`


### Additional Resources

- 📖 [Official FastAPI Documentation](https://fastapi.tiangolo.com/)
- 🎥 [FastAPI YouTube Tutorials](https://www.youtube.com/results?search_query=fastapi+tutorial)
- 💬 [FastAPI Discord Community](https://discord.com/invite/VQjSZaeJmf)
- 📚 [Pydantic Documentation](https://docs.pydantic.dev/)
- 🔧 [Uvicorn Documentation](https://www.uvicorn.org/)

### Quiz

Test your knowledge:

1. What command do you use to run a FastAPI application?
2. What is the default URL for Swagger UI documentation?
3. How do you define a path parameter in FastAPI? 
4. What is the purpose of type hints in FastAPI?
5.  What is Uvicorn and why do we need it?

**Answers:**
1. `uvicorn main:app --reload`
2. `http://127.0.0. 1:8000/docs`
3. Using curly braces: `/items/{item_id}`
4. Automatic data validation and better IDE support
5. Uvicorn is an ASGI server needed to run FastAPI applications

---

## 🎯 Checklist

Before moving to Module 2, ensure you can:

- [ ] Explain what FastAPI is and its key features
- [ ] Set up a Python virtual environment
- [ ] Install FastAPI and Uvicorn
- [ ] Create a basic FastAPI application
- [ ] Define GET routes with path parameters
- [ ] Add query parameters to endpoints
- [ ] Run the application with Uvicorn
- [ ] Access and use Swagger UI documentation
- [ ] Add metadata to enhance documentation
- [ ] Organize endpoints using tags

---

**Congratulations! 🎉 You've completed Module 1!**

Ready to continue?  Move on to [Module 2: Core Concepts](module_02_core_concepts.md)