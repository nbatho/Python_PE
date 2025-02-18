for _ in range(int(input())):
    ls = []
    n = int(input())
    for i in range(n):
        a,b = map(int,input().split())
        ls.append((a,b))
    ls.sort(key=lambda x: x[1])
    i=0
    cnt=1
    for j in range(1,n):
        if ls[j][0] >= ls[i][1]:
            cnt+=1
            i=j
    print(cnt)