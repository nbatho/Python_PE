def sum_(n):
    tong = 0
    for i in range(len(n)):
        tong += int(n[i])
    return tong
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    sum_num = []
    for i in range(n):
        for j in range(i+1,n):
            if sum_(str(a[i])) > sum_(str(a[j])):
                a[i],a[j] = a[j],a[i]
            elif sum_(str(a[i])) == sum_(str(a[j])):
                if a[i] > a[j]:
                    a[i],a[j] = a[j],a[i]
    for i in a:
        print(i,end = " ")
    print()