def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


def find_highest_number(numbers):
    if not numbers:
        return None

    highest = numbers[0]

    for number in numbers:
        if number > highest:
            highest = number

    return highest


def count_words(sentence):
    words = sentence.split()
    return len(words)


def count_item_frequency(items):
    frequency = {}

    for item in items:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1

    return frequency


def get_passing_students(students, pass_mark=50):
    passing_students = []

    for student in students:
        if student["grade"] >= pass_mark:
            passing_students.append(student)

    return passing_students

def find_lowest_number(numbers):
    # Return the lowest number in the list.
    # If the list is empty, return None.
    if not numbers:
        return None
    
    lowest = numbers[0]
    
    for number in numbers:
        if number < lowest:
            lowest = number

    return lowest


def get_students_above_average(students):
    # Return a list of students whose grade is above the class average.
    if not student:
        return None
    
    student_above_avg = []
    
    grade_avg = sum(student["grade"] for student in students) / len(students)

    for student in students:

        if student["grade"] > grade_avg:
            student_above_avg.append(student)

    return student_above_avg
            

def sort_students_by_grade(students):
    # Return students sorted from highest grade to lowest grade.
    if not students:
        return None
        
    return sorted(students, key=lambda student: student["grade"], reverse=True)



def count_pass_and_fail(students, pass_mark=50):
    # Return a dictionary like:
    # {"pass": 3, "fail": 1}

    if not students:
        return {"pass": 0, "fail": 0}

    pass_fail_count = {
        "pass" : 0,
        "fail" : 0
    }

    for student in students:
        if student["grade"] < pass_mark:
            pass_fail_count["fail"] += 1
        else:
            pass_fail_count["pass"] += 1

    return pass_fail_count

def main():
    numbers = [10, 20, 30, 40, 50]
    sentence = "Python is useful for backend and data analysis"
    items = ["Python", "SQL", "Python", "Java", "SQL", "Python"]

    students = [
        {"name": "Ali", "grade": 82},
        {"name": "Sara", "grade": 91},
        {"name": "Omar", "grade": 47},
        {"name": "Lina", "grade": 65}
    ]

    print("Average:", calculate_average(numbers))
    print("Highest:", find_highest_number(numbers))
    print("Word count:", count_words(sentence))
    print("Frequency:", count_item_frequency(items))
    print("Passing students:", get_passing_students(students))

    print("Lowest:", find_lowest_number(numbers))
    print("Students above average:", get_students_above_average(students))
    print("Students sorted by grade:", sort_students_by_grade(students))
    print("Pass/fail count:", count_pass_and_fail(students))

if __name__ == "__main__":
    main()