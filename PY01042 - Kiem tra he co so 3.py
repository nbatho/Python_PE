def CheckBase3(n):
    for i in range(0,len(n)):
        if n[i] != '0' and n[i] != '1' and n[i] != '2':
            return False
    return True
for _ in range(int(input())):
    n = input()
    if CheckBase3(n): print("YES")
    else :print("NO")
