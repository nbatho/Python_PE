n = []
cnt = 0
seen = set
while True:
    values = input().split()
    cnt += len(values)
    tmp = 0
    for i in values:
        tmp = int(i) % 42
        if tmp not in n: n.append(tmp)
    if cnt == 10: break
print(len(n))
