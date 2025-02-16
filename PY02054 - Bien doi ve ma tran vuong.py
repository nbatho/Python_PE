n , m = map(int,input().split())

a = []
for i in range(n):
    x = list(map(int,input().split()))
    a.append(x)
num = abs(n-m)
cnt = 0

if n > m:
    hang = []
    for i in range(n):
        if i % 2 == 0:
            hang.append(i)
            cnt += 1
            if cnt == num: break           
    for i in range(n):
        if i not in hang:
            for j in range(m):
                print(a[i][j],end = " ")
            print()

elif m > n:
    cot = []
    for j in range(m):
        if j % 2 != 0:
            cot.append(j)
            cnt += 1
            if cnt == num:break
    for i in range(n):
        for j in range(m):
            if j not in cot:
                print(a[i][j],end = " ")
        print()
else:
    for i in range(n):
        for j in range(m):
            print(a[i][j],end = " ")
        print()