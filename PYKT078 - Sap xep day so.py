for _ in range(int(input())):
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    max_value = max(a)
    for i in range(n):
        if a[i] == max_value:
            a.insert(i,m)
            break
    am = []
    duong = []
    for i in range(n + 1):
        if a[i] < 0: am.append(a[i])
        else: duong.append(a[i])
    for num in am:
        print(num,end = " ")
    for num in duong:
        print(num,end = " ")
    print()
