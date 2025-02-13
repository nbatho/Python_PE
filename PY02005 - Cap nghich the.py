n =int(input())
cnt =0
a=list(map(int,input().split()))
for i in range(n-1):
    for j in range(i+1,n):
        if a[i]>a[j]:cnt+=1
print(cnt)