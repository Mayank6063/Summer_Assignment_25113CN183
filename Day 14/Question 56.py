n = int(input("Enter size of array: "))
arr = []

for i in range(n):
    arr.append(int(input()))

duplicates = []

for i in range(n):
    for j in range(i + 1, n):
        if arr[i] == arr[j] and arr[i] not in duplicates:
            duplicates.append(arr[i])

print("Duplicate elements:", duplicates)