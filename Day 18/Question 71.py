a = [1, 2, 3, 4, 5]
x = 4

l = 0
h = len(a) - 1

while l <= h:
    m = (l + h) // 2

    if a[m] == x:
        print("Found")
        break
    elif a[m] < x:
        l = m + 1
    else:
        h = m - 1