a = [[1,4,6],
     [3,5,7],
     [6,8,4]]
b = [[6,8,4],
      [4,6,8],
      [4,0,6]]
c=[[0,0,0],[0,0,0],[0,0,0]]
for i in range (len(a)):
    for j in range (len(a[0])):
        c[i][j] = a[i][j]-b[i][j]
print(c)