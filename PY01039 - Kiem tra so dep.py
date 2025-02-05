def check(n):
    for i in range(0,len(n) - 2):
        if n[i] != n[i+2] : return False
    return True
for i in range(int(input())):
    n = input()
    if (check(n)): print("YES")
    else: print("NO")