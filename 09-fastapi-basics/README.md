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

## Day 9: SQLite Integration

In Day 9, I connected the FastAPI app to the existing SQLite database.

The API now reads real internship application data from:

```text
placement.db


## SQLite Endpoints
GET /applications
GET /applications/{application_id}
GET /applications/search/by-status?status=Interested
GET /applications/search/by-company?company=Google

## What I Practised
Connecting FastAPI to SQLite
Reusing database logic from the CLI project
Converting sqlite3.Row objects into dictionaries
Returning real database records as JSON
Using fetchone() for one record by ID
Using fetchall() for search/list endpoints
Raising HTTPException with 404 when a record is not found

## Day 10: POST Endpoint and Pydantic Validation

In Day 10, I added the first write endpoint to the API.

The API can now create new internship applications using:

```text
POST /applications

What the POST Endpoint Does
Client sends JSON body
FastAPI validates the data using Pydantic
The API checks for duplicates
The application is inserted into SQLite
The new application is returned as JSON

Validation Added
The request body is validated using a Pydantic model.

Required fields:

    company
    role_title
    location
    work_mode
    status

Allowed work modes:

    Hybrid
    Remote
    On-site

Allowed statuses:

    Interested
    Applied
    Interview
    Rejected
    Offer

Error Handling
201 Created -> New application created successfully
409 Conflict -> Duplicate application
422 Validation Error -> Invalid request body

What I Practised
Creating a POST endpoint
Using Pydantic BaseModel
Validating request body data
Using Literal for allowed values
Inserting new rows into SQLite
Using cursor.lastrowid
Returning the newly created record
Handling duplicate data with HTTPException

## Day 11: PATCH Endpoint for Status Updates

In Day 11, I added an update endpoint to change the status of an internship application.

The API can now update an application using:

```text
PATCH /applications/{application_id}/status


## Example request body:

{
  "status": "Interview"
}

## What the PATCH Endpoint Does
Client sends the application ID in the URL
Client sends the new status in the request body
Pydantic validates the status
SQLite updates the application row
The API checks cursor.rowcount
The updated application is returned as JSON

## What I Practised
Creating a PATCH endpoint
Updating one field instead of the whole record
Using a Pydantic model for update validation
Running SQL UPDATE from FastAPI
Using cursor.rowcount to detect missing records
Returning the updated row after the update

## Day 12: Refactor into Multiple Files

In Day 12, I refactored the FastAPI project from one large file into a cleaner multi-file structure.

### New Structure

```text
app/
├── __init__.py
├── main.py
├── database.py
├── models.py
└── crud.py

main.py      API routes and HTTP error handling
database.py  SQLite connection and row conversion helpers
models.py    Pydantic request models
crud.py      SQL database functions