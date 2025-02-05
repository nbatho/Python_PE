n = input()

res = ""
cnt = 0
i = len(n) - 1
while (i != 0):
    res += n[i]
    cnt+=1
    if cnt == 3:
        res += ","
        cnt = 0
    i -=1
res += n[0]

i = len(res) - 1

while (i != -1):
    print(res[i],end="")
    i-=1
