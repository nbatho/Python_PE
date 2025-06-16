def Count(n,h):
    ans = 0
    for i in range(0,n):
        tong = 0
        so = i
        while so != 0:
            tong += so % 10
            so //= 10
        if tong == h:
            ans += 1
    print(ans)
while True:
    s = input()
    if s == "-1":
        break
    n,h = s.split()
    Count(int(n),int(h))