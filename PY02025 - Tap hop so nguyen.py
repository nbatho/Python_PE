n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort()
giao = []
i, j = 0, 0
while i < n and j < m:
    if a[i] == b[j]:
        if not giao or giao[-1] != a[i]: 
            giao.append(a[i])
        i += 1
        j += 1
    elif a[i] < b[j]:
        i += 1
    else:
        j += 1
set_a = set(a)
set_b = set(b)
hieu_a = sorted(set_a - set_b)
hieu_b = sorted(set_b - set_a)
print(*giao)
print(*hieu_a)
print(*hieu_b)