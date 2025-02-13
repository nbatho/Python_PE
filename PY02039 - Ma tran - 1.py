a = []
n = int(input())
for i in range(n):
    x = list (map(int,input().split()))
    a.append(x)
chinh = 0
phu = 0
for i in range(n):
    for j in range(n):
        if i<j:
            chinh += a[i][j]
        elif i>j:
            phu +=a[i][j]

k = int(input())
if k > abs(chinh-phu): print("YES")
else:print("NO")
print(abs(chinh-phu))