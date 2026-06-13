import numpy as np

def even_numbers(arr):
    return arr[arr%2 == 0]

arr = np.array(list(map(int, input("Enter array elements: ").split())))

ans = even_numbers(arr)

print(ans)