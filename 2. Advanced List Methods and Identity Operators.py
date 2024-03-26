# Task 1: Given the two lists

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

submitted_and_attended = []

for student in submitted:
    if student in attended:
        submitted_and_attended.append(student)

#print(submitted_and_attended)


# Task 2: Check if the two lists are identical in terms of their content, regardless of order.

lists_same = True;

for student in submitted:
    if student in attended:
        continue
    else:
        lists_same = False
        break

#print(lists_same)

# Task 3: Using list methods, remove any student from the attended list who did not submit their assignment.

for student in attended:
    if student not in submitted:
        attended.remove(student)

#print(attended)