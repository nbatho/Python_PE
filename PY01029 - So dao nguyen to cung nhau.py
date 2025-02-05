def GCD(a,b):
    while b != 0:
        tmp = b
        b = a % b 
        a = tmp
    return a
def CheckNguyenToCungNhau(a,b):
    return GCD(a,b) == 1
for i in range(int(input())):
    n = input()
    dao = ""
    for i in range(len(n) - 1, -1,-1):
        dao+= n[i]
    if CheckNguyenToCungNhau(int(n), int(dao)): print("YES")
    else:print("NO")