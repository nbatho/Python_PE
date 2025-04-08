n,m,x = [int (num) for num in input().split()]
vs = [False] * (n + 1)
ls = [[] for _ in range(n + 1)]
duyet = []
def DFS(u):
    vs[u] = True
    duyet.append(u)
    for v in ls[u]:
        if not vs[v]:
            DFS(v)

for i in range(m):
    u,v = [int (num) for num in input().split()]
    ls[u].append(v)
    ls[v].append(u)

DFS(x)
for i in range(1,n+1):
    if i not in duyet:
        print(i)
