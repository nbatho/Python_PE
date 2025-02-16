for _ in range(int(input())):
    s = input()
    n = input()
    cnt = 0
    vs = [False]*len(s)
    for i in range(0,len(s) - len(n) + 1):
        tmp = ""
        if (vs[i] == False):
            for j in range(i,i+len(n)):
                tmp += s[j]
                if tmp == n:
                    for i in range(i,i+len(n)):
                        vs[i] = True
                    cnt += 1

    print(cnt)
