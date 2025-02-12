n = int(input())
ls = list(map(int,input().split()))
ls.sort()
for i in ls:
    if i + 1 not in ls:
        print(i+1)
        break