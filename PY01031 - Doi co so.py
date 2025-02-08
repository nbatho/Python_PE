for _ in range(int(input())):
    n, b = map(int,input().split())
    ans = ""
    while n != 0:
        mod = n%b
        if mod < 10:
            ans += str(mod)
        else: ans += chr(ord("A") + (mod - 10))
        n //=b 
    print(ans[::-1])
