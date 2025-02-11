def Try(ans,n,a,b,c):
    if len(ans) == n and a > 0 and a <= b and b <= c:
        print(ans)
    
    if len(ans) < n:
        Try(ans + "A",n,a+1,b,c)
        Try(ans + "B",n,a,b+1,c)
        Try(ans + "C",n,a,b,c+1)


n = int(input())
for i in range(3,n+1):
    Try("",i,0,0,0)
