def Convert(x,b,bac):
    fullbinary = ""
    if len(x) % bac != 0:
        for i in range(0,bac - len(x) % bac):
            fullbinary += "0"
    x = fullbinary + x
    i = len(x) - 1
    cnt = 0
    bin = ""
    ans = ""
    while i != -1:
        bin += x[i]
        cnt += 1
        num = 0
        if cnt == bac:
            for j in range(0,len(bin)):
                num += (2**j) * int(bin[j])
            if num < 10:
                ans += str(num)
            else:
                ans += chr(ord("A") + (num -10))
            num = 0
            cnt = 0
            bin = ""
        i-=1
    print(ans[::-1])

data = open("DATA.in","r")
for _ in range(int(data.readline())):
    b = int(data.readline())
    x = data.readline().strip()
    bac = 0
    if b == 2:
        print(x)
    else:
        if b == 4: bac = 2
        elif b == 8: bac = 3
        elif b == 16: bac = 4
        Convert(x,b,bac)

data.close()
