from app.database import connect_to_database, row_to_dict, rows_to_dicts


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

def delete_application_from_db(application_id):
    connection = connect_to_database()
    cursor = connection.cursor()

    cursor.execute(
        """
        DELETE FROM applications
        WHERE id = ?;
        """,
        (application_id,)
    )

    connection.commit()
    rows_deleted = cursor.rowcount
    connection.close()

    return rows_deleted