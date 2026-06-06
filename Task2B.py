def principal_sum(matrix):
    sum = 0
    for i in range(len(matrix)):
        sum += matrix[i][i]
    return sum

def secondary_sum(matrix):
    sum = 0
    for i in range(len(matrix)):
        sum += matrix[i][len(matrix)-i-1]
    return sum


r = int(input("Enter number of rows: "))
#c = int(input("Enter number of columns: "))
matrix = []
for i in range(r):
    row = list(map(int, input().split()))
    matrix.append(row)

ans = secondary_sum(matrix)
print(ans)