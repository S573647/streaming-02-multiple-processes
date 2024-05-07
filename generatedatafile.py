import csv
import random

# List of sample student names
student_names = ["Alice", "Bob", "Charlie", "David", "Emma", "Frank", "Grace", "Hannah", "Ivy", "Jack"]

# List of sample courses
courses = ["Mathematics", "Science", "History", "English", "Computer Science"]

# Generate random grades for each student and course
data = []
for student in student_names:
    for course in courses:
        grade = round(random.uniform(60, 100), 2)  # Random grade between 60 and 100
        data.append([student, course, grade])

# Write data to a CSV file
with open("student_grades.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Student Name", "Course", "Grade"])  # Write header row
    writer.writerows(data)  # Write data rows
