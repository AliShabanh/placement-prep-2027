import sqlite3


DATABASE_NAME = "placement.db"


def connect_to_database():
    connection = sqlite3.connect(DATABASE_NAME)
    connection.row_factory = sqlite3.Row
    return connection


def get_all_applications():
    connection = connect_to_database()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM applications;")
    applications = cursor.fetchall()

    connection.close()
    return applications

def get_applications_by_status(status):
    connection = connect_to_database()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT *
        FROM applications
        WHERE status = ?;
        """,
        (status,)
    )

    applications = cursor.fetchall()
    connection.close()

    return applications

def application_exists(company, role_title):
    connection = connect_to_database()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT *
        FROM applications
        WHERE company = ?
          AND role_title = ?;
        """,
        (company, role_title)
    )

    application = cursor.fetchone()
    connection.close()

    return application is not None

def add_application(company, role_title, location, work_mode, status, deadline, applied_date, salary, notes):
    if application_exists(company, role_title):
        print(f"Application already exists: {company} - {role_title}")
        return

    connection = connect_to_database()
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO applications
        (company, role_title, location, work_mode, status, deadline, applied_date, salary, notes)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
        """,
        (company, role_title, location, work_mode, status, deadline, applied_date, salary, notes)
    )

    connection.commit()
    connection.close()

    print(f"Application added: {company} - {role_title}")

def update_application_status(application_id, new_status):
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

    if rows_updated == 0:
        print(f"No application found with ID {application_id}.")
    else:
        print(f"Application {application_id} status updated to {new_status}.")

def get_applications_by_company(company):
    connection = connect_to_database()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT *
        FROM applications
        WHERE company = ?;
        """,
        (company,)
    )

    applications = cursor.fetchall()
    connection.close()

    return applications

def display_applications(applications):
    if not applications:
        print("No applications found.")
        return

    print("-" * 60)

    for application in applications:
        print(f"ID: {application['id']}")
        print(f"Company: {application['company']}")
        print(f"Role: {application['role_title']}")
        print(f"Location: {application['location']}")
        print(f"Work mode: {application['work_mode']}")
        print(f"Status: {application['status']}")
        print(f"Deadline: {application['deadline']}")
        print("-" * 60)


def main():
    add_application(
        company="Intel",
        role_title="Software Engineering Intern",
        location="Leixlip",
        work_mode="Hybrid",
        status="Interested",
        deadline="2026-11-10",
        applied_date=None,
        salary="Unknown",
        notes="Good company for software, hardware, and engineering roles"
    )

    print("\nAll applications:")
    all_applications = get_all_applications()
    display_applications(all_applications)

    print("\nInterested applications:")
    interested_applications = get_applications_by_status("Interested")
    display_applications(interested_applications)

    print("\nUpdating application status...")
    update_application_status(1, "Applied")

    print("\nApplied applications:")
    applied_applications = get_applications_by_status("Applied")
    display_applications(applied_applications)

    print("\nApplications for Google:")
    google_applications = get_applications_by_company("Google")
    display_applications(google_applications)


if __name__ == "__main__":
    main()