a = [[2,5,7],
     [8,9,7],
     [6,7,8]]

r = [[0,0,0],
     [0,0,0],
     [0,0,0]]

for i in range(len(a)):
    for j in range(len(a[0])):
        r[j][i] = a[i][j]

for row in r:
    print(row)
