import sqlite3
from typing import Literal, Optional

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field


DATABASE_NAME = "placement.db" # SQLite database

VALID_STATUSES = ["Interested", "Applied", "Interview", "Rejected", "Offer"]
VALID_WORK_MODES = ["Hybrid", "Remote", "On-site"]

app = FastAPI(title="Internship Tracker API")

class ApplicationCreate(BaseModel):
    company: str = Field(..., min_length=1)
    role_title: str = Field(..., min_length=1)
    location: str = Field(..., min_length=1)
    work_mode: Literal["Hybrid", "Remote", "On-site"]
    status: Literal["Interested", "Applied", "Interview", "Rejected", "Offer"]
    deadline: Optional[str] = None
    applied_date: Optional[str] = None
    salary: str = "Unknown"
    notes: Optional[str] = None

class ApplicationStatusUpdate(BaseModel):
    status: Literal["Interested", "Applied", "Interview", "Rejected", "Offer"]

def connect_to_database():
    connection = sqlite3.connect(DATABASE_NAME)
    connection.row_factory = sqlite3.Row
    return connection

def row_to_dict(row): # converts sqlite3.Row to Dict
    return dict(row)

def rows_to_dicts(rows):
    return [row_to_dict(row) for row in rows]

@app.get("/")
def root():
    return {
        "message": "Internship Tracker API connected to SQLite"
    }


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "database": DATABASE_NAME
    }

def get_all_applications_from_db():
    connection = connect_to_database()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT *
        FROM applications
        ORDER BY deadline ASC;
        """
    )

    applications = cursor.fetchall()
    connection.close()

    return rows_to_dicts(applications)

def get_application_by_id_from_db(application_id):
    connection = connect_to_database()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT *
        FROM applications
        WHERE id = ?;
        """,
        (application_id,)
    )

    application = cursor.fetchone()
    connection.close()

    if application is None:
        return None

    return row_to_dict(application)

def get_applications_by_company_from_db(company):
    connection = connect_to_database()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT *
        FROM applications
        WHERE LOWER(company) LIKE LOWER(?)
        ORDER BY deadline ASC;
        """,
        (f"%{company}%",)
    )

    applications = cursor.fetchall()
    connection.close()

    return rows_to_dicts(applications)

def get_applications_by_status_from_db(status):
    connection = connect_to_database()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT *
        FROM applications
        WHERE LOWER(status) = LOWER(?)
        ORDER BY deadline ASC;
        """,
        (status,)
    )

    applications = cursor.fetchall()
    connection.close()

    return rows_to_dicts(applications)

def application_exists_in_db(company, role_title):
    connection = connect_to_database()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT *
        FROM applications
        WHERE LOWER(TRIM(company)) = LOWER(TRIM(?))
          AND LOWER(TRIM(role_title)) = LOWER(TRIM(?));
        """,
        (company, role_title)
    )

    application = cursor.fetchone()
    connection.close()

    return application is not None

def add_application_to_db(application):
    connection = connect_to_database()
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO applications
        (company, role_title, location, work_mode, status, deadline, applied_date, salary, notes)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
        """,
        (
            application.company,
            application.role_title,
            application.location,
            application.work_mode,
            application.status,
            application.deadline,
            application.applied_date,
            application.salary,
            application.notes
        )
    )

    connection.commit()
    new_application_id = cursor.lastrowid
    connection.close()

    return new_application_id

def update_application_status_in_db(application_id, new_status):
    connection = connect_to_database()
    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE applications
        SET status = ?
        WHERE id = ?;
        """,
        (new_status, application_id)
    )

    connection.commit()
    rows_updated = cursor.rowcount
    connection.close()

    return rows_updated

@app.post("/applications", status_code=status.HTTP_201_CREATED)
def create_application(application: ApplicationCreate):
    if application_exists_in_db(application.company, application.role_title):
        raise HTTPException(
            status_code=409,
            detail="Application already exists"
        )

    new_application_id = add_application_to_db(application)
    new_application = get_application_by_id_from_db(new_application_id)

    return new_application

@app.get("/applications")
def get_applications():
    return get_all_applications_from_db()

@app.patch("/applications/{application_id}/status")
def update_application_status(
    application_id: int,
    status_update: ApplicationStatusUpdate
):
    rows_updated = update_application_status_in_db(
        application_id,
        status_update.status
    )

    if rows_updated == 0:
        raise HTTPException(
            status_code=404,
            detail="Application not found"
        )

    updated_application = get_application_by_id_from_db(application_id)

    return updated_application

@app.get("/applications/{application_id}")
def get_application(application_id: int):
    application = get_application_by_id_from_db(application_id)

    if application is None:
        raise HTTPException(status_code=404, detail="Application not found")

    return application

@app.get("/applications/search/by-status")
def search_applications_by_status(status: str):
    return get_applications_by_status_from_db(status)

@app.get("/applications/search/by-company")
def search_applications_by_company(company: str):
    return get_applications_by_company_from_db(company)