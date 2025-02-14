n = int(input())
cnt = 0
a = []
while True:
    x = input().split()
    cnt += len(x)
    for i in x:
        a.append(int(i))
    if cnt == n:break

chan = []
le = []
idx = [0]*n
for i in range(n):
    if a[i] % 2 == 0:
        chan.append(a[i])
    else:
        le.append(a[i])
        idx[i] = 1
chan.sort()
le.sort(reverse= True)
idxeven = 0
idxodd = 0
ans = []
for i in range(n):
    if idx[i] == 0:
        ans.append(chan[idxeven])
        idxeven +=1
    elif idx[i] == 1:
        ans.append(le[idxodd])
        idxodd+=1
print(*ans)