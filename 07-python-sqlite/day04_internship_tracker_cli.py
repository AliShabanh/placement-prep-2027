import sqlite3

DATABASE_NAME = "placement.db"


def connect_to_database():
    connection = sqlite3.connect(DATABASE_NAME)
    connection.row_factory = sqlite3.Row
    return connection


def get_all_applications():
    connection = connect_to_database()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM applications ORDER BY deadline ASC;")
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

def add_application_from_input():
    print("\nAdd New Application")
    print("-" * 30)

    company = input("Company: ").strip()
    role_title = input("Role title: ").strip()

    if not company or not role_title:
        print("Company and role title are required.")
        return

    if application_exists(company, role_title):
        print(f"Application already exists: {company} - {role_title}")
        return

    location = input("Location: ").strip()
    work_mode = input("Work mode (Hybrid/Remote/On-site): ").strip()
    status = input("Status (Interested/Applied/Interview/Rejected/Offer): ").strip()
    deadline = input("Deadline (YYYY-MM-DD): ").strip()
    applied_date = input("Applied date (YYYY-MM-DD or leave blank): ").strip()
    salary = input("Salary/pay info or Unknown: ").strip()
    notes = input("Notes: ").strip()

    if applied_date == "":
        applied_date = None

    if not location or not work_mode or not status:
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


def show_menu():
    print("\nInternship Tracker")
    print("=" * 30)
    print("1. View all applications")
    print("2. Add application")
    print("3. Search by status")
    print("4. Search by company")
    print("5. Update application status")
    print("6. Exit")


def main():
    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            applications = get_all_applications()
            display_applications(applications)

        elif choice == "2":
            add_application_from_input()

        elif choice == "6":
            print("Goodbye.")
            break

        else:
            print("Invalid choice. Please choose a number from 1 to 6.")


if __name__ == "__main__":
    main()