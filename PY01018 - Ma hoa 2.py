P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."

while True:
    string = input()

    if string == "0": break

    k , s = string.split()
    k = int(k)
    res = ""
    for i in range(0,len(s)):
        for j in range(0,len(P)):
            if (s[i] == P[j]):
                res += P[(j+k)%28]
    for i in range(0,len(res)):
        print(res[len(res) - i - 1],end = "")
    print()
    