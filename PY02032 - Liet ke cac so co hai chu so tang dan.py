s = input()
cnt = 0
num = ""
ans = []
for i in range(len(s)):
    num += s[i]
    cnt += 1
    if cnt == 2:
        if int(num) not in ans:
            ans.append(int(num))
        cnt = 0
        num = ""
ans.sort()
for i in ans:
    print(i,end = " ")