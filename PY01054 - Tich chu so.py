for _ in range(int(input())):
    n = input()
    ans = 1
    for i in range(0,len(n)):
        if (int(n[i]) !=0):
            ans *= int(n[i])
    print(ans)