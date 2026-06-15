n = int(input("Enter size of array: "))

arr = []

for i in range(n):
    arr.append(int(input()))

even = 0
odd = 0

for i in arr:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even elements =", even)
print("Odd elements =", odd)
