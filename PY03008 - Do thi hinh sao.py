n = int(input())
ls = [[] for i in range(n+1)]
vs = [False] * (n+1)
def BFS(u):
    q = []
    q.append(u)
    vs[u] = True
    cnt = 1
    while len(q) > 0:
        x = q.pop()
        for v in ls[x]:
            if vs[v] == False:
                q.append(v)
                vs[v] = True
                cnt+=1 
    return cnt
for i in range(n-1):
    x,y = [int(val) for val in input().split()]
    ls[x].append(y)
    ls[y].append(x)
ans = []
for i in range(1,n+1):
    ans.append(BFS(i))
ok = True
for i in ans:
    if i != 1 and i != n:
        ok = False
        break
if ok: print("Yes")
else:print("No")

