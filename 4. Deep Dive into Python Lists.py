# Task 1: Given the lists

students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]

under_80_students = []
for grade in grades:
    if grade < 80:
        student_index = grades.index(grade)
        under_80_students.append(students[student_index])
        under_80_students.append(grades[student_index])
        under_80_students.append(activities[student_index])

#print(under_80_students)

# Task 2: For the remaining students, add students name in a new list named students_approved. Expected Outcome: students_approved = ["John", "Doe", "Smith"]

students_approved = []
for student in students:
    if student is not under_80_students[0]:
        students_approved.append(student)

#print(students_approved)


# Task 3: Print the list students_approved

print(students_approved)