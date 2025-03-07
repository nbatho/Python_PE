n = int(input())
ls = []
for _ in range(n-1):
    ls.append(int(input()))
cnt = 1

ls.sort()
for i in ls:
    if i != cnt:
        print(cnt)
        break
    else: cnt += 1