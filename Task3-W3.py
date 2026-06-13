import numpy as np

def max_sum_row(matrix):
    sum_list = np.sum(matrix, axis = 1)
    return np.argmax(sum_list)

r = int(input("Enter number of rows: "))

matrix = []
for i in range(r):
    row = list(map(int, input(f"Enter elements of row {i + 1} separated by space: ").split()))
    matrix.append(row)

matrix = np.array(matrix)
print(max_sum_row(matrix))