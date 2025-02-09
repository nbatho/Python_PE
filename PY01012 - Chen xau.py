s1 = input()
s2 = input()
p = int(input()) - 1

ans = ""
for i in range(0,len(s1)):
    ans += s1[i]
    if i == p - 1:
        ans += s2
print(ans)

