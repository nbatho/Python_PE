ls = []
while True:
    try:
        x = input().split()
        for data in x:
            ls.append(int(data))
    except EOFError:
        break
idx = 0
t = ls[idx]
idx += 1

for _ in range(t):
    n = ls[idx]
    m = ls[idx+1]
    idx += 2
    a = [[0 for _ in range(m)] for _ in range(n)]
    cv = []
    for i in range(n):
        for j in range(m):
            a[i][j] = ls[idx]
            idx+=1
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