def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    ans = []

    for j in range(cols):
        row = []
        for i in range(rows):
            row.append(matrix[i][j])
        ans.append(row)
    return ans

r = int(input("Enter number of rows: "))
c = int(input("Enter number of columns: "))
matrix = []
print("Enter matrix elements row wise: ")
for i in range(r):
    row = list(map(int, input().split()))
    matrix.append(row)

t = transpose(matrix)
print("Transpose: ")
for row in t:
    print(*row)

