# FastAPI Basics

This folder contains my first FastAPI practice app.

The goal was to understand how an API works before connecting it to a database.

## What I Built

- Root endpoint
- Health check endpoint
- Get all applications endpoint
- Get one application by ID endpoint
- Search applications by status endpoint
- Proper 404 error handling using HTTPException

## Technologies Used

- Python
- FastAPI
- Uvicorn

## How to Run

From the root of the repository, activate the virtual environment:

```bash
.venv\Scripts\activate
```

Then run:

```bash
fastapi dev 09-fastapi-basics/main.py
```

Open the API:

```text
http://127.0.0.1:8000
```

Open the interactive docs:

```text
http://127.0.0.1:8000/docs
```

## Endpoints

```text
GET /                                  Root welcome message
GET /health                            API health check
GET /applications                      Get all applications
GET /applications/{application_id}     Get one application by ID
GET /applications/search/by-status     Search applications by status
```

## What I Learned

- How to create a FastAPI app
- How to run a local development server
- How to return JSON responses
- How to use path parameters
- How to use query parameters
- How to raise a 404 error with HTTPException
- How FastAPI automatically creates interactive API documentation

## Next Step

Connect FastAPI to the existing SQLite internship tracker database.