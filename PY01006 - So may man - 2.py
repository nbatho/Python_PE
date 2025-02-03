def LuckyNumber(n):
    diff = 0
    for i in range(0, len(n)):
        if n[i] != '4' and n[i] != '7':
            diff = 1
            break
    return diff == 0

tc = int(input())
for i in range(0,tc):
    n = input()
    if LuckyNumber(n): print("YES")
    else: print("NO")


