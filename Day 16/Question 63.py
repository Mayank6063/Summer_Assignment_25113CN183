arr = [1, 4, 5, 6, 3, 2]
target = 7

seen = set()

for num in arr:
    if target - num in seen:
        print("Pair:", target - num, num)
    seen.add(num)