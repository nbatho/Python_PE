def dao(n):
    s = ""
    for i in range(len(n) - 1, -1,-1):
        s+= n[i]
    return s
for i in range(int(input())):
    n = int(input())
    while n % 7 != 0:
        n += int(dao(str(n)))
    
    print(n)
    

