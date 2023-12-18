import numpy as np 
sx, sy = 0, 0
dx, dy = 3, 4
x, y = dx-sx, dy-sy
m =np.zeros((x, y))
m[0,] = 1
m[:, 0]=1
print(m)


    
for i in range(x):
    for j in range(y):
        if(i == 0 or j == 0): continue
        else:
            p, q = m[i-1][j], m[i][j-1]
            m[i][j] =  p + q

print("\n\nthe path count matrix \n", m, "\n paths:")




def findpaths(mat, i, j, m, n, path, pi):
    if(i == m-1):
        for k in range(j, n):
            path[pi+ k - j] = mat[i][k]
        for l in range(pi + n - j):
            print(path[l], end = " ")
        print()
        return

    if (j == n - 1):
 
        for k in range(i, m):
            path[pi + k - i] = mat[k][j]
 
        for l in range(pi + m - i):
            print(path[l], end = " ")
        print()
        return
    
    path[pi] = mat[i][j]
    findpaths(mat, i + 1, j, m, n, path, pi + 1)
    findpaths(mat, i, j + 1, m, n, path, pi + 1)

def printAllPaths(mat, x, y):
 
    path = [0 for i in range(x + y)]
    findpaths(mat, 0, 0, x, y, path, 0)

printAllPaths(m, x, y)