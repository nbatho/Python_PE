# dem so phan tu max lien tiep
n = int(input()) + 1
a = [int(x) for x in input().split()] + [-1]
max_value = max(a)
cnt = 0 
ans = 0
for i in range(n):
    if a[i] == max_value:
        cnt += 1
    else:
        ans = max(ans,cnt)
        cnt = 0

print(ans)