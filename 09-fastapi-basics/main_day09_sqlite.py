import sqlite3
from fastapi import FastAPI, HTTPException


DATABASE_NAME = "placement.db" # SQLite database

app = FastAPI(title="Internship Tracker API")

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

@app.get("/applications")
def get_applications():
    return get_all_applications_from_db()


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