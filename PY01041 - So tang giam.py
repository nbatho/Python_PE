def CheckGiam(n):
    for i in range(0,len(n) - 1):
        if n[i] < n[i+1]: return False
    return True
for _ in range(int(input())):
    n = input()
    if CheckGiam(n): print("NO")
    else:
        Idx = 0
        pos = 0
        found = True
        for i in range(0,len(n)):
            if int(n[i]) > Idx:
                # print(i,n[i], sep = " ",end = "\n")
                Idx = int(n[i])
            else: 
                pos = i
                break

        for i in range(pos - 1, len(n) - 1):
            if n[i] < n[i+1]:
                found = False
                break
        if found == True: print("YES")
        else: print("NO")