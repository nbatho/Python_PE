ls = []
n = int(input())
for i in range(n):
    s = input()
    

    i = 0
    num = ""
    while i < len(s):
        if s[i] >= "0" and s[i] <= "9":
            num += s[i]
        else:
            if len(num) > 0:
                ls.append(int(num))
                num = ""
        i+=1
    if len(num) > 0:

        ls.append(int(num))
        num = ""

ls.sort()
for i in ls:
    print(i)