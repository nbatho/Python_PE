def DFS(a, u, n, vs, path, ls):
    path.append(u)
    vs[u] = True
    if u == n:
        ls.append(path.copy())
    else:
        for v in a[u]:
            if not vs[v]:
                DFS(a, v, n, vs, path, ls)
    path.pop()
    vs[u] = False

for _ in range(int(input())):
    v, e, s, n = map(int, input().split())
    a = [[] for _ in range(v + 1)]
    for _ in range(e):
        x, y = map(int, input().split())
        a[x].append(y)
    vs = [False] * (v + 1)
    ls = []
    maxVal = 0
    DFS(a, s, n, vs, [], ls)
    dd = [0]*10000
    for i in range(len(ls)):
        for j in range(len(ls[i])):
            dd[ls[i][j]]+=1
            maxVal = max(maxVal,dd[ls[i][j]])
    ans = 0
    for i in range(v):
        if i != s and i != n and dd[i] > len(ls) - 1:
            ans +=1
    print(ans)
    

