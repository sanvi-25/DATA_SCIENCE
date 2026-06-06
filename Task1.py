def count_unique(arr):
    unique = []
    for ele in arr:
        if ele not in unique:
            unique.append(ele)

    return unique

arr = list(map(int, input("Enter elements separated y spaces: ").split()))

result = count_unique(arr)
print("Unique elements are: ", result)
