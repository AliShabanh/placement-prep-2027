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