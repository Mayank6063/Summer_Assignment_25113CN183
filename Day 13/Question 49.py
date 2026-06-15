n = int(input("Enter size of array: "))

arr = []

for i in range(n):
    num = int(input())
    arr.append(num)

print("Array elements are:")
for i in arr:
    print(i, end=" ")