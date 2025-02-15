def Convert(x1,x2,s):
    ans = ""
    for i in range(len(s)):
        if s[i] == x1:
            s[i] = x2
    for i in range(len(s)):
        if s[i] >= "0" and s[i] <= "9":
            ans +=s[i]
    return ans
for _ in range(int(input())):
    x1,x2 = input().split()
    s = input().split()
    s1 = []
    s2 = []
    if len(s) > 1:
        a,b = s
    else:
        a = s[0]
        b = input()
    for i in a: s1.append(i)
    for i in b: s2.append(i)

    minVal = 0
    minVal += int(Convert(x2,x1,s1))
    minVal += int(Convert(x2,x1,s2))
    maxVal = 0
    maxVal += int(Convert(x1,x2,s1))
    maxVal += int(Convert(x1,x2,s2))

    print(min(minVal,maxVal),max(minVal,maxVal))