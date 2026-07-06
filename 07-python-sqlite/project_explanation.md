# Internship Tracker CLI — Project Explanation

## Problem

When applying for internships, it is easy to lose track of companies, roles, deadlines, application statuses, and notes.

This project solves that problem by storing internship applications in a local SQLite database and allowing the user to manage them through a command-line menu.

## Solution

I built a Python command-line application that connects to a SQLite database.

The user can:

- View all internship applications
- View one application by ID
- Add new applications
- Search by status
- Search by company
- Update application status

## Main Program Flow

The app follows this pattern:

```text
menu → user input → validation → database operation → result displayed to user
```

## Important Concepts I Used

### SQLite Database

The app stores data in a local SQLite database called:

```text
placement.db
```

The main table is:

```text
applications
```

### Database Connection

The app uses `sqlite3.connect()` to connect Python to the SQLite database.

### Cursor

A cursor is used to run SQL commands such as:

```sql
SELECT
INSERT
UPDATE
```

### Fetching Data

`fetchall()` is used when multiple rows may be returned.

Example:

```text
View all applications
Search by status
Search by company
```

`fetchone()` is used when only one row is expected.

Example:

```text
View application by ID
Check if an application already exists
```

### Commit

`commit()` is used after database changes such as:

```text
INSERT
UPDATE
```

This saves the change to the database.

### Parameterised Queries

The app uses `?` placeholders instead of putting user input directly into SQL strings.

This keeps SQL commands separate from user input and helps avoid SQL injection problems.

### Validation

The app validates:

- Required text fields
- Application ID
- Allowed statuses
- Allowed work modes
- Duplicate applications

## What I Learned

I learned how to:

- Connect Python to SQLite
- Create reusable database functions
- Retrieve rows using `fetchone()` and `fetchall()`
- Insert new records
- Update existing records
- Validate user input
- Use `rowcount` to check if an update affected a row
- Refactor code into clearer sections
- Build a small command-line app from database logic

## How This Connects to FastAPI

This project prepares me for building a backend API.

The current functions can later become API endpoints:

```text
get_all_applications()       → GET /applications
get_application_by_id()      → GET /applications/{id}
add_application()            → POST /applications
update_application_status()  → PATCH /applications/{id}/status
```

## Future Improvements

- Split the code into multiple files
- Add automated tests
- Add delete functionality
- Add update notes functionality
- Add date validation
- Convert this CLI app into a FastAPI backend
- Use PostgreSQL instead of SQLite later

## Project Status

The command-line version is working. This project is the foundation for a future FastAPI internship tracker API.