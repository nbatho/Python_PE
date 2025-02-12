n = int(input())
a = list(map(float,input().split()))
a.sort()
tb = 0
min_val = a[0]
max_val = a[0]
for i in a:
    min_val = min(min_val,i)
    max_val = max(max_val,i)
cnt = 0
for i in a:
    if i != min_val and i != max_val:
        tb += i
        cnt += 1

print("%.2f" % (tb/cnt))
