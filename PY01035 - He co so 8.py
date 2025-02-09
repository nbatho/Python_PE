n = input()
fullbinary = ""
if len(n) % 3 != 0:
    for i in range(0, 3 - len(n) % 3):
        fullbinary += "0"
    n = fullbinary + n
i = len(n) - 1
cnt = 0
bin = ""
ans = ""
while (i != -1):
    bin += n[i]
    cnt += 1
    num = 0
    if cnt % 3 == 0:
        for j in range(len(bin) - 1,-1, -1):
            num += (2**j) * int(bin[j])
        ans += str(num)
        bin = ""
    i -=1
print(ans[::-1])

