# Internship Tracker CLI

A command-line Python application for tracking internship applications.

This project was built as part of my placement preparation. The goal was to practise Python, SQLite, SQL queries, input validation, and basic backend-style logic before moving into FastAPI.

## Features

- View all internship applications
- View one application by ID
- Add a new application
- Prevent duplicate applications
- Search applications by status
- Search applications by company
- Update application status
- Validate status and work mode inputs
- Store data locally using SQLite

## Technologies Used

- Python
- SQLite
- sqlite3
- Git and GitHub

## Project Structure

```text
07-python-sqlite/
├── day03_python_sqlite.py
├── day04_internship_tracker_cli.py
├── day05_internship_tracker_refactor.py
├── project_explanation.md
└── README.md
```

## How to Run

From the root of the repository, run:

```bash
python 07-python-sqlite/day05_internship_tracker_refactor.py
```

Or on Windows:

```bash
py 07-python-sqlite/day05_internship_tracker_refactor.py
```

## Menu Options

```text
Internship Tracker
==============================
1. View all applications
2. View application by ID
3. Add application
4. Search by status
5. Search by company
6. Update application status
7. Exit
```

## Database

The app uses a local SQLite database called:

```text
placement.db
```

The main table is:

```text
applications
```

Main columns:

- id
- company
- role_title
- location
- work_mode
- status
- deadline
- applied_date
- salary
- notes

## What I Practised

- Connecting Python to SQLite
- Creating reusable database functions
- Using SQL queries such as SELECT, INSERT, UPDATE, WHERE, LIKE, and ORDER BY
- Using fetchone() when one row is expected
- Using fetchall() when multiple rows may be returned
- Using parameterised SQL queries with ? placeholders
- Using commit() after database changes
- Validating user input
- Using rowcount to check whether an update affected a row
- Refactoring code into clearer sections

## Code Structure

The final CLI file is organised into clear sections:

- Database connection
- Validation helpers
- Database operations
- User interface functions
- Main program loop

## Key Backend Concepts

This project follows a backend-style flow:

```text
user input → validation → database operation → result displayed to user
```

The same logic can later be converted into FastAPI endpoints:

```text
get_all_applications()       → GET /applications
get_application_by_id()      → GET /applications/{id}
add_application()            → POST /applications
update_application_status()  → PATCH /applications/{id}/status
```

## Future Improvements

- Split database logic and user interface into separate files
- Add delete application feature
- Add update notes feature
- Add date validation
- Add automated tests
- Convert the project into a FastAPI backend API
- Replace SQLite with PostgreSQL later

## Project Status

Working CLI version completed. This project is a foundation for a future FastAPI internship tracker API.