
def CheckDK(s):
    n = int(s)
    sum = 0
    while n != 0:
        sum += n%10
        n = int(n/10)
    if sum % 10 != 0: return False
    for i in range(0,len(s) - 1):
        if abs(int(s[i]) - int(s[i+1])) != 2 : return False
    return True
    
for i in range(int(input())):
    n = input()
    if (CheckDK(n)): print("YES")
    else: print("NO")