# ==============================
# Student Course Tracker
# Starter Template
# ==============================

# Starter data (DO NOT MODIFY)
students = [
    ("Alice", 20),
    ("Bob", 22),
    ("Charlie", 21)
]

courses = ["Python", "JavaScript", "Python", "Databases"]

student_data = {
    "Alice": {"courses": ["Python", "Databases"], "grades": [85, 90]},
    "Bob": {"courses": ["Python", "JavaScript"], "grades": [78, 82]},
    "Charlie": {"courses": ["JavaScript"], "grades": [88]}
}

# ------------------------------
# Task 1: Remove Duplicate Courses
# ------------------------------
unique_courses = set(courses)
print("Unique courses:", unique_courses)


# ------------------------------
# Task 2: Display Student Info
# ------------------------------
for name, age in students:
    enrolled_courses = student_data[name]["courses"]
    print(name, "-", age, "years old,", "Courses:", enrolled_courses)


# ------------------------------
# Task 3: Add Course for Bob
# ------------------------------
if "Databases" not in student_data["Bob"]["courses"]:
    student_data["Bob"]["courses"].append("Databases")

print("Bob's updated courses:", student_data["Bob"]["courses"])


# ------------------------------
# Task 4: Calculate Average Grades
# ------------------------------
for name in student_data:
    grades = student_data[name]["grades"]
    average = sum(grades) / len(grades)
    print(name, "average grade:", average)


# ------------------------------
# Task 5: Find Students in a Course
# ------------------------------
course_name = input("Enter a course name: ")

for name in student_data:
    if course_name in student_data[name]["courses"]:
        print(name, "is enrolled in", course_name)


# ------------------------------
# Bonus (Optional)
# ------------------------------
highest_average = 0
top_student = ""

for name in student_data:
    grades = student_data[name]["grades"]
    average = sum(grades) / len(grades)
    student_data[name]["average"] = average

    if average > highest_average:
        highest_average = average
        top_student = name

print("Top student:", top_student, "with average grade:", highest_average)
