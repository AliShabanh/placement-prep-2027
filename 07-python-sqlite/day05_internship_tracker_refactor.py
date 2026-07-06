# Day 4: Command-line internship tracker
# This app connects to a SQLite database and allows the user to:
# - view internship applications
# - add new applications
# - search by status
# - search by company
# - update application status
# Note: This application was developed with AI assistance as a learning project.
# The goal is to better understand how Python connects to and interacts with
# SQLite while practicing the implementation of real-world database operations.
# Any code in the "08-independent-practice" folder represents my own independent
# work and practice without AI-generated implementations.
import sqlite3


DATABASE_NAME = "placement.db"

VALID_STATUSES = [
    "Interested",
    "Applied",
    "Interview",
    "Rejected",
    "Offer"
]

VALID_WORK_MODES = [
    "Hybrid",
    "Remote",
    "On-site"
]

# -----------------------------
# Database connection
# -----------------------------

def connect_to_database():
    connection = sqlite3.connect(DATABASE_NAME)
    connection.row_factory = sqlite3.Row
    return connection

# -----------------------------
# Validation helpers
# -----------------------------

def is_valid_status(status):
    return status in VALID_STATUSES


def is_valid_work_mode(work_mode):
    return work_mode in VALID_WORK_MODES


def display_valid_statuses():
    print("Valid statuses:")
    for status in VALID_STATUSES:
        print(f"- {status}")


def display_valid_work_modes():
    print("Valid work modes:")
    for work_mode in VALID_WORK_MODES:
        print(f"- {work_mode}")

def is_required_text(value):
    return bool(value.strip())

def get_valid_application_id():
    application_id_text = input("Enter application ID: ").strip()

    if not application_id_text.isdigit():
        print("Application ID must be a number.")
        return None

    return int(application_id_text)

# -----------------------------
# Database operations
# -----------------------------

def get_all_applications():
    connection = connect_to_database()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM applications ORDER BY deadline ASC;")
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
        WHERE LOWER(status) = LOWER(?)
        ORDER BY deadline ASC;
        """,
        (status,)
    )

    applications = cursor.fetchall()
    connection.close()

    return applications

def get_applications_by_company(company):
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

    return applications

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

    return rows_updated

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

def get_application_by_id(application_id):
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

    return application

# -----------------------------
# User interface functions
# -----------------------------

def add_application_from_input():
    print("\nAdd New Application")
    print("-" * 30)

    company = input("Company: ").strip()
    role_title = input("Role title: ").strip()

    if not is_required_text(company) or not is_required_text(role_title):
        print("Company and role title are required.")
        return

    if application_exists(company, role_title):
        print(f"Application already exists: {company} - {role_title}")
        return

    location = input("Location: ").strip()
    display_valid_work_modes()
    work_mode = input("Work mode: ").strip()

    if not is_valid_work_mode(work_mode):
        print("Invalid work mode. Please use one of the valid work modes.")
        return
    
    display_valid_statuses()
    status = input("Status: ").strip()

    if not is_valid_status(status):
        print("Invalid status. Please use one of the valid statuses.")
        return
    
    deadline = input("Deadline (YYYY-MM-DD): ").strip()
    applied_date = input("Applied date (YYYY-MM-DD or leave blank): ").strip()
    salary = input("Salary/pay info or Unknown: ").strip()
    notes = input("Notes: ").strip()

    if applied_date == "":
        applied_date = None

    if not is_required_text(location) or not is_required_text(work_mode) or not is_required_text(status):
        print("Location, work mode, and status are required.")
        return

    add_application(
        company=company,
        role_title=role_title,
        location=location,
        work_mode=work_mode,
        status=status,
        deadline=deadline,
        applied_date=applied_date,
        salary=salary if salary else "Unknown",
        notes=notes
    )

def search_by_status_from_input():
    print("\nSearch by Status")
    print("-" * 30)

    status = input("Enter status (Interested/Applied/Interview/Rejected/Offer): ").strip()

    if not status:
        print("Status is required.")
        return

    applications = get_applications_by_status(status)
    display_applications(applications)

def search_by_company_from_input():
    print("\nSearch by Company")
    print("-" * 30)

    company = input("Enter company name or part of company name: ").strip()

    if not company:
        print("Company search text is required.")
        return

    applications = get_applications_by_company(company)
    display_applications(applications)

def update_status_from_input():
    print("\nUpdate Application Status")
    print("-" * 30)

    application_id = get_valid_application_id()

    if application_id is None:
        return
    
    display_valid_statuses()

    new_status = input("Enter new status: ").strip()

    if not is_valid_status(new_status):
        print("Invalid status. Please use one of the valid statuses.")
        return

    rows_updated = update_application_status(application_id, new_status)

    if rows_updated == 0:
        print(f"No application found with ID {application_id}.")
    else:
        print(f"Application {application_id} status updated to {new_status}.")

def view_application_by_id_from_input():
    print("\nView Application by ID")
    print("-" * 30)

    application_id = get_valid_application_id()

    if application_id is None:
        return

    application = get_application_by_id(application_id)

    if application is None:
        print(f"No application found with ID {application_id}.")
        return

    display_applications([application])

# -----------------------------
# Main program loop
# -----------------------------

def show_menu():
    def show_menu():
        print("\nInternship Tracker")
        print("=" * 30)
        print("1. View all applications")
        print("2. View application by ID")
        print("3. Add application")
        print("4. Search by status")
        print("5. Search by company")
        print("6. Update application status")
        print("7. Exit")


def main():
    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            applications = get_all_applications()
            display_applications(applications)

        elif choice == "2":
            view_application_by_id_from_input()

        elif choice == "3":
            add_application_from_input()

        elif choice == "4":
            search_by_status_from_input()

        elif choice == "5":
            search_by_company_from_input()

        elif choice == "6":
            update_status_from_input()

        elif choice == "7":
            print("Goodbye.")
            break

        else:
            print("Invalid choice. Please choose a number from 1 to 7.")


if __name__ == "__main__":
    main()