def check(n):
    if len(n)%2 == 0 or n[0] == n[1] :return False
    for i in range(2,len(n),2):
        if n[i] != n[0] : return False
    return True
for _ in range(int(input())):
    n = input()    
    if (check(n)): print("YES")
    else: print("NO")