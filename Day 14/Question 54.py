n = int(input("Enter size of array: "))
arr = []

for i in range(n):
    arr.append(int(input()))

x = int(input("Enter element: "))

count = 0

for i in arr:
    if i == x:
        count += 1

print("Frequency =", count)