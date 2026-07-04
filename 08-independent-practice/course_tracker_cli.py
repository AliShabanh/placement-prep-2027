# This version was developed entirely by me.
# The only external reference I used was my code from Day 04.
import sqlite3

DATABASE_NAME = "course_tracker.db"

VALID_STATUSES = ["Not started", "In progress", "Completed", "Failed"]

def connect_to_database():
    connection = sqlite3.connect(DATABASE_NAME)
    connection.row_factory = sqlite3.Row
    return connection

def get_all_courses():
    connection = connect_to_database()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM courses;")
    courses = cursor.fetchall()
    connection.close()

    return courses

def course_exists(module_name, teacher):

    connection = connect_to_database()
    cursor = connection.cursor()

    cursor.execute(
        """
        
        SELECT *
        FROM courses
        WHERE LOWER(TRIM(module_name)) = LOWER(TRIM(?))
            AND LOWER(TRIM(teacher)) = LOWER(TRIM(?));

        """,
        (module_name, teacher)

    )

    courses = cursor.fetchone()
    connection.close()

    return courses is not None


def add_course_input():

    print("\nAdd New Course")
    print("-" * 30)

    module_name = input("Enter Module Name: ").strip()
    teacher = input("Enter Teacher Name: ").strip()

    if not module_name or not teacher:
        print("Module name and teacher are required.")
        return

    if course_exists(module_name, teacher):
        print(f"Course already Exists: {module_name} - {teacher}")
        return

    semester = input("Enter semester: ").strip()
    status = input("Enter Status(Not started/In progress/Completed/Failed): ").strip()

    if status not in VALID_STATUSES:
        print("Invalid status. Use one of the valid statuses.")
        return

    grade = input("Enter grade: ").strip()
    notes = input("Notes: ").strip()

    if not notes:
        notes = ""

    if not semester or not grade:
        print("Semester and Grade are required.")
        return
    
    connection = connect_to_database()
    cursor = connection.cursor()
    
    cursor.execute(
        """

        INSERT INTO courses
        (module_name, teacher, semester, status, grade, notes)
        VALUES(?,?,?,?,?,?);
        
        """,
        (module_name, teacher, semester, status, grade, notes)
        
    )

    connection.commit()
    connection.close()

    print(f"Course added: {module_name} with teacher: {teacher}")
def get_course_by_status():

    status = input("Enter Status(Not started/In progress/Completed/Failed): ").strip()

    if not status:
        print("Status required")
        return
    
    if status not in VALID_STATUSES:
        print("Invalid Status, use one of the Valid Status")
        return
    
    connection = connect_to_database()
    cursor = connection.cursor()

    cursor.execute(
        """

        SELECT *
        FROM courses
        WHERE LOWER(status) = LOWER(?);

        """, 
        (status,)
        
    )

    courses = cursor.fetchall()
    connection.close()

    display_courses(courses)

def get_course_by_teacher():
    teacher_name = input("Enter teacher name: ").strip()

    if not teacher_name:
        print("Teacher name is required.")
        return
    
    connection = connect_to_database()
    cursor = connection.cursor()

    cursor.execute(
        """

        SELECT *
        FROM courses
        WHERE LOWER(teacher) LIKE LOWER(?);

        """, 
        (f"%{teacher_name}%",)
        
    )

    courses = cursor.fetchall()
    connection.close()

    display_courses(courses)

def update_course_status():

    print("\nUpdate Course Status")
    print("-" * 30)

    course_id_text = input("Enter the course ID: ").strip()

    if not course_id_text.isdigit():
        print("Course ID must be a number")
        return
    
    course_id = int(course_id_text)
    new_status = input("Enter Status(Not started/In progress/Completed/Failed): ").strip()

    if new_status not in VALID_STATUSES:
        print("Invalid status. Please use one of the valid statuses.")
        return
    
    connection = connect_to_database()
    cursor = connection.cursor()

    cursor.execute(
        """

        UPDATE courses
        SET status = ?
        WHERE id = ?;

        """,
        (new_status, course_id)
    )

    connection.commit()
    rows_updated = cursor.rowcount
    connection.close()

    if rows_updated == 0:
        print(f"No course found with ID {course_id}.")
    else:
        print(f"Course {course_id} status updated to {new_status}.")

    return rows_updated

def display_courses(courses):
    if not courses:
        print("No Courses found.")
        return
    
    print("-" * 60)

    for course in courses:
        print(f"ID: {course['id']}")
        print(f"Module name: {course['module_name']}")
        print(f"Teacher name: {course['teacher']}")
        print(f"Semester 1 / 2: {course['semester']}")
        print(f"Status: {course['status']}")
        print(f"Grade: {course['grade']}")
        print(f"Notes: {course['notes']}")
        print("-"* 60)

def menu():
     
    print("Course Tracker")
    print("=" * 30)
    print("1. View all courses")
    print("2. Add course")
    print("3. Search by status")
    print("4. Search by teacher")
    print("5. Update course status")
    print("6. Exit")
    


def main():

    while True:

        menu()
        choice = input("Choose an Option: ").strip()

        if choice == "1":
            all_courses = get_all_courses()
            display_courses(all_courses)

        elif choice == "2":
            add_course_input()
        elif choice == "3":
            get_course_by_status()
        elif choice == "4":
            get_course_by_teacher()
        elif choice == "5":
            update_course_status()
        elif choice == "6":
            print("SEE YOU LATER")
            break

        else: 
            print("Invalid Input, Please choose a number between 1-6.")

        
if __name__ == "__main__":
    main()
