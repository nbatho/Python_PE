# TLE :)
for _ in range(int(input())):
    n,m,l = map(int,input().split())

    a = [[0] * (m+1)] * (n+1)
    for i  in range(1,n+1):
        x = list(map(int,input().split()))
        a[i] = [0] + x

    for i in range(1,n+1):
        for j in range(1,m+1):
            a[i][j] += a[i-1][j] + a[i][j-1] - a[i-1][j-1]   
    for i in range(n-l+1):
        for j in range(m-l+1):  
            ans =(a[i+l][j+l] - a[i+l][j] - a[i][j+l] + a[i][j])
            ans //=(l*l)
            print(ans,end = " ")
        print()