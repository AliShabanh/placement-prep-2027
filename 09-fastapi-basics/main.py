from fastapi import FastAPI, HTTPException


app = FastAPI()

applications = [
    {
        "id": 1,
        "company": "Microsoft",
        "role_title": "Software Engineering Intern",
        "location": "Dublin",
        "status": "Interested"
    },
    {
        "id": 2,
        "company": "Google",
        "role_title": "STEP Intern",
        "location": "Dublin",
        "status": "Interested"
    },
    {
        "id": 3,
        "company": "IBM",
        "role_title": "Data and AI Intern",
        "location": "Dublin",
        "status": "Applied"
    }
]


@app.get("/")
def root():
    return {"message": "Welcome to my FastAPI app"}

@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "message": "API is running"
    }

@app.get("/applications")
def get_applications():
    return applications

@app.get("/applications/{application_id}")
def get_application(application_id: int):
    for application in applications:
        if application["id"] == application_id:
            return application

    raise HTTPException(status_code=404, detail="Application not found")

@app.get("/applications/search/by-status")
def search_applications_by_status(status: str):
    matching_applications = []

    for application in applications:
        if application["status"].lower() == status.lower():
            matching_applications.append(application)

    return matching_applications