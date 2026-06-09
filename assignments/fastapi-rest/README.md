# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a small, well-structured REST API using the FastAPI framework. Students will implement CRUD endpoints, use Pydantic models for validation, and run the app with Uvicorn.

## 📝 Tasks

### 🛠️ Project Setup

#### Description
Create a new Python project directory and prepare the environment to run a FastAPI app.

#### Requirements

- Install dependencies from `requirements.txt`.
- Create a working `starter-code.py` that launches a FastAPI app.

### 🛠️ Implement CRUD Endpoints

#### Description
Implement endpoints to Create, Read, Update, and Delete an `Item` resource.

#### Requirements

- Implement `GET /items` to list all items.
- Implement `GET /items/{item_id}` to retrieve a single item by id.
- Implement `POST /items` to create a new item using a Pydantic model.
- Implement `PUT /items/{item_id}` to update an existing item.
- Implement `DELETE /items/{item_id}` to remove an item.

### 🛠️ Data Models and Validation

#### Description
Use Pydantic models to validate request and response data.

#### Requirements

- Define an `Item` model with at least `id`, `name`, and optional `description` fields.
- Validate inputs and return appropriate HTTP status codes for invalid data.

### 🛠️ Documentation & Running the App

#### Description
Provide instructions to run the app and use the automatic API docs.

#### Requirements

- Include commands to install dependencies and start the server.
- Verify the interactive docs are available at `/docs` and the OpenAPI JSON at `/openapi.json`.

## Starter Files

- `starter-code.py` — Minimal FastAPI application with in-memory storage and CRUD endpoints.
- `requirements.txt` — Python dependencies for the project.

## How to run

1. Create and activate a virtual environment (optional but recommended).
2. Install dependencies:

```
pip install -r requirements.txt
```

3. Run the app with Uvicorn:

```
uvicorn starter-code:app --reload
```

4. Open interactive docs at `http://127.0.0.1:8000/docs`.

## Learning Resources

- FastAPI official docs: https://fastapi.tiangolo.com/
- Uvicorn docs: https://www.uvicorn.org/
