def CheckNonDec(s):
    for i in range(0, len(s) - 1): 
        if s[i] > s[i + 1]:
            return False
    return True
tc = int(input())
for i in range(0,tc):
    s = input()
    if (CheckNonDec(s)): print("YES")
    else: print("NO")