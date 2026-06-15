n = int(input("Enter size of array: "))
arr = []

for i in range(n):
    arr.append(int(input()))

arr = arr[-1:] + arr[:-1]

print("After Right Rotation:")
print(arr)