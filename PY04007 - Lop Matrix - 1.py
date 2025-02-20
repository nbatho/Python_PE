for _ in range(int(input())):
    n,m = map(int,input().split())
    a = [[0]*m]*n
    cv = []
    for i in range(n):
        a[i] = [int (x) for x in input().split()]
    for i in range(m):
        x = []
        for j in range(n):
            x.append(a[j][i])
        cv.append(x)
    for i in range(n):
        for j in range(n):
            s = 0
            for k in range(m):
                s += a[i][k]* cv[k][j]
            print(s,end = " ")
        print()