for _ in range(int(input())):
    n , d = map(int,input().split())
    a = list(map(int,input().split()))
    for i in range(d, len(a)):
        print(a[i],end = " ")
    for i in range(0,d):
        print(a[i],end = " ")
    print()
    