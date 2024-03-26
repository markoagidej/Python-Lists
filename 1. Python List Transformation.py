# Task 1: Given the list of grades

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades.sort()
grades.reverse()
print(grades)


# Task 2: Calculate the average grade and display it.

grades_sum = sum(grades)
grades_average = grades_sum / len(grades)
print(grades_average)

# Task 3: Replace any grade below 80 with the value Failed.

index = 0
for grade in grades:
    if grade < 80:
        grades[index] = "Failed"
    index += 1

# print(grades)