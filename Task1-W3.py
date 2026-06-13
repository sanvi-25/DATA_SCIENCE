import numpy as np

def result(arr):
    print("Sum =", np.sum(arr))
    print("Mean =", np.mean(arr))
    print("Max =", np.max(arr))

arr = np.array(list(map(int, input("Enter elements: ").split())))

result(arr)