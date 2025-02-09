def Try(n,k):
    while n > 0:
        len = 2**n - 1
        mid = (len + 1) // 2
        if mid == k: return n - 1
        elif k < mid: n-=1
        else:
            k-=mid
            n-=1    
for _ in range(int(input())):
    n,k = map(int,input().split())
    ans = ord("A") + Try(n,k)
    print(chr(ans))