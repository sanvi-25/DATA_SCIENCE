import numpy as np

def detect_traffic(matrix):
    avg = np.mean(matrix)
    curr = np.mean(matrix, axis = 1)

    result = []

    for i in range(len(curr)):
        if(curr[i] > 2*avg):
            result.append(i)

    return result

r = int(input("Enter number of rows: "))
c = int(input("Enter number of columns: "))
matrix = []
for i in range(r):
    row = list(map(int, input(f"Enter data for row {i+1}: ").split()))
    matrix.append(row)

matrix = np.array(matrix)
print(detect_traffic(matrix))