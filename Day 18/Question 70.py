a = [5, 3, 8, 1, 2]

for i in range(len(a)):
    small = i

    for j in range(i+1, len(a)):
        if a[j] < a[small]:
            small = j

    temp = a[i]
    a[i] = a[small]
    a[small] = temp

print(a)