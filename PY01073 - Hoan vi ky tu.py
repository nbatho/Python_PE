s = input()

n = len(s)
used = [False]* (n)

def Try(i,ans):
    if  i == n:
        print(ans)
        return
    for j in range(n):
        if used[j] == False:
            used[j] = True
            Try(i+1,ans + s[j])
            used[j] = False

Try(0,"")