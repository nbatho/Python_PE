def prod_(n):
    tich = 1
    for i in range(len(n)):
        tich *= int(n[i])
    return tich
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    prod_num = []
    for i in range(n):
        for j in range(i+1,n):
            if prod_(str(a[i])) > prod_(str(a[j])):
                a[i],a[j] = a[j],a[i]
            elif prod_(str(a[i])) == prod_(str(a[j])):
                if a[i] > a[j]:
                    a[i],a[j] = a[j],a[i]
    for i in a:
        print(i,end = " ")
    print()