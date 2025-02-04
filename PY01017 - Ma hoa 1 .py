tc = int(input())
for _ in range(0,tc):
    s = input()
    idx = 0
    cnt = 1
    for i in range(1,len(s)):
        kytu = s[idx]
        if kytu == s[i]:
            cnt+= 1
        elif kytu != s[i]:
            print(cnt,kytu,sep ="", end ="")
            cnt = 1
            idx = i 
    print(cnt, s[idx], sep="")
