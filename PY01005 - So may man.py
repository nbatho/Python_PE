def LuckyNumber(n):
    cnt4, cnt7 = 0, 0  
    for i in range(0,len(n)):
        if n[i] == '4': cnt4+=1
        elif n[i] == '7': cnt7+=1
    return cnt4 + cnt7 == 4 or cnt4 + cnt7 == 7

n = input()

if (LuckyNumber(n)): print("YES")
else: print("NO")