n = int(input())
data = []
date = []
for _ in range(n):

    s = input().split()
    if s[4] not in date: date.append(s[4])
    if s[4] not in data and s[3] == "IN":
        if s[1] == "Xe_con":
            if s[2] == "5":
                data.append((s[4],10000))
            elif s[2] == "7":
                data.append((s[4],15000))
        elif s[1] == "Xe_tai" and s[2] == "2":
            data.append((s[4],20000))
        elif s[1] == "Xe_khach":
            if s[2] == "29":
                data.append((s[4],50000))
            elif s[2] == "45":
                data.append((s[4],70000))

for i in date:
    sum = 0
    for first,second in data:
        if i == first:
            sum += int(second)
    print(f'{i}: {sum}')