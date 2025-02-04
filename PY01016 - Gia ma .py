tc = int(input())
for i in range(0,tc):
    s = input()
    for i in range(1 ,len(s)):
        if (s[i] >= "0" and s[i] <= "9"):
            cnt = int(s[i])
            while (cnt):
                print(s[i-1],end ="")
                cnt -=1
    print()
