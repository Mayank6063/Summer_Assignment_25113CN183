n = int(input("Enter size of array: "))
arr = []

for i in range(n):
    arr.append(int(input()))

arr.reverse()

print("Reversed Array:")
print(arr)