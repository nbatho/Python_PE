def HNTower(n,a,b,c):
    int(n)
    if n == 1: 
        print(a,c,sep = " -> ")
    else:
        HNTower(n-1,a,c,b)
        print(a,c,sep = " -> ")
        HNTower(n-1,b,a,c)
n = int(input())
HNTower(n,'A','B','C')
