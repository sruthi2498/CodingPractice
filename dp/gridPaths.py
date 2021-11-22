def getAllPathsInGrid(n,m):
    opt=[ [0 for _ in range(m)] for _ in range(n) ]
    paths = [ [[] for _ in range(m)] for _ in range(n) ]
    paths[0][0]=[""]
    for i in range(1,n):
        opt[i][0]=1
        for p in paths[i-1][0]:
            paths[i][0].append("V"+p)
    for j in range(1,m):
        opt[0][j]=1
        for p in paths[0][j-1]:
            paths[0][j].append("H"+p)
    for i in range(1,n):
        for j in range(1,m):
            opt[i][j] = opt[i-1][j]+opt[i][j-1]
            for p in paths[i-1][j]:
                paths[i][j].append(p+"V")
            for p in paths[i][j-1]:
                paths[i][j].append(p+"H")

    for row in paths:
        print(row)
    return sorted(paths[n-1][m-1])

print(getAllPathsInGrid(3,2))