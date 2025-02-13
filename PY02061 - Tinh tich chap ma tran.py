dx = [-1,-1,-1,0,0,0,1,1,1]
dy = [-1,0,1,-1,0,1,-1,0,1]
for _ in range(int(input())):
    m,n = map(int,input().split())
    x = [[0]]*m
    h = [[0]]*3
    for i in range(m):
        x[i] =list ( map(int,input().split()))
    for i in range(3):
        h[i] = list(map(int,input().split()))
    matrix = []
    sum = 0
    for i in range(3):
        for j in range(3):
            matrix.append(int(h[i][j]))
    for i in range(2, m) :
        for j in range(2, n) :
            sum +=  x[i - 2][j - 2] * h[0][0] 
            sum +=  x[i - 2][j - 1] * h[0][1]
            sum +=  x[i - 2][j] * h[0][2]
            sum +=  x[i - 1][j - 2] * h[1][0]
            sum +=  x[i - 1][j - 1] * h[1][1]
            sum +=  x[i - 1][j] * h[1][2]
            sum +=  x[i][j - 2] * h[2][0]
            sum +=  x[i][j - 1] * h[2][1]
            sum +=  x[i][j] * h[2][2]
    print(sum)