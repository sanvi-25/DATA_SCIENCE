import numpy as np

def top_students(marks):
    avg = np.mean(marks, axis=1)

    result = []
    for i in range(len(avg)):
        if avg[i] > 75:
            result.append(i)

    return result

r = int(input("Enter number of students: "))
c = int(input("Enter number of subjects: "))

marks = []

for i in range(r):
    row = list(map(int, input(f"Enter marks of student {i}: ").split()))
    marks.append(row)

marks = np.array(marks)

print(top_students(marks))