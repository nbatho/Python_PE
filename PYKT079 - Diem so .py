for _ in range(int(input())):
    n = int(input())
    a = []
    danhdau = [0]*1001
    x = map(int,input().split())
    for i in x:
        a.append(int(i))
        danhdau[i] = 1
    r = min(a)
    l = max(a)
    idx = 0
    cnt = 0
    for i in range(r, l+ 1):
        if danhdau[i] == 0:
            cnt += 1
    print(cnt)