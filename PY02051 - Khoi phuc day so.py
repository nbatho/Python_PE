n = int(input())
ls = []
for i in range(n):
    ls.append([int(x) for x in input().split()])
ans = []
if n > 2:
    a = (ls[0][1] + ls[0][2] - ls[1][2]) //2
    ans.append(a)
    for i in range(1,n):
        val = abs(ls[i][0] - a)
        ans.append(val)
    print(*ans)
else:
    print(ls[0][1]//2,ls[1][0]//2)

