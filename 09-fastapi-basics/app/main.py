from fastapi import FastAPI, HTTPException, status

from app.crud import (
    add_application_to_db,
    application_exists_in_db,
    get_all_applications_from_db,
    get_application_by_id_from_db,
    get_applications_by_company_from_db,
    get_applications_by_status_from_db,
    update_application_status_in_db,
)
from app.database import DATABASE_NAME
from app.models import ApplicationCreate, ApplicationStatusUpdate


app = FastAPI(title="Internship Tracker API")


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


@app.get("/applications")
def get_applications():
    return get_all_applications_from_db()


@app.get("/applications/search/by-status")
def search_applications_by_status(status: str):
    return get_applications_by_status_from_db(status)


@app.get("/applications/search/by-company")
def search_applications_by_company(company: str):
    return get_applications_by_company_from_db(company)


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
        raise HTTPException(
            status_code=404,
            detail="Application not found"
        )

    return application