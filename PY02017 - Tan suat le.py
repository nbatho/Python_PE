for _ in range(int(input())):
    n = int(input())
    a = []
    x = input().split()
    for i in x:
        a.append(int(i))
    danhdau = [0]*100001
    for i in range(n):
        danhdau[a[i]] +=1
    
    for i in range(0,100001):
        if danhdau[i] % 2 !=0:
            print(i)