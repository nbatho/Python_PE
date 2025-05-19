def dfs(u, vs, adj):
    vs[u] = 1
    for v in adj[u]:
        if not vs[v]:
            dfs(v, vs, adj)

for _ in range(int(input())):
    v, e = map(int, input().split())    
    adj = [[int(x) for x in input().split()] for _ in range(e)]
    maxv = 1
    ans = 0
    for i in range(1,v+1):
        newadj = [[] for _ in range(v + 1)]
        vs = [0] * (v + 1)
        for x,y in adj:
            if x != i and y != i:
                newadj[x].append(y)
                newadj[y].append(x)
        cnt = 0
        for j in range(1, v + 1): 
            if j != i and not vs[j]:
                dfs(j, vs, newadj)
                cnt += 1
        if maxv < cnt:
            ans = i
            maxv = max(maxv,cnt)

    print(ans)
