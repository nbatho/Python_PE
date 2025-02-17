for _ in range(int(input())):
    n = int(input())
    used = [False]* (n)
    a = [0] * n
    ls = []
    def Try(i):
        for j in range(n-1,-1,-1):
            if (used[j] == False):
                a[i] = j
                used[j] = True
                if i == n - 1:
                    ans = ""
                    for k in range(0,n):
                        ans += str(a[k]+1)
                    if ans:
                        ls.append(ans)
                else: Try(i+1)
                used[j] = False

    Try(0)
    print(len(ls))
    print(*ls)