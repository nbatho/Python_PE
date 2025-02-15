s = input()
cnt = 0
num = ""
danhdau = [0]*101
a = []
for i in range(len(s)):
    num += s[i]
    cnt += 1
    if cnt == 2:
        danhdau[int(num)] +=1
        if int(num) not in a:
            a.append(int(num))
        cnt = 0
        num = ""

pair = []
for i in  a:
    for j in range(0,101):
        if j == i:
            print(i,danhdau[i])