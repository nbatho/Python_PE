def GCD(a, b):
    while b != 0:
        tmp = b
        b = a % b
        a = tmp 
    return a

def CheckNguyenToCungNhau(a,b):
    return GCD(a,b) == 1

n, k = map(int,input().split())

start = 10**(k-1) - 1
end = 10**k 
cnt = 0
for i in range(start,end):
    if (CheckNguyenToCungNhau(i,n)):
        print(i,sep =" ", end = " ")
        cnt+=1
    if cnt == 10:
        print()
        cnt = 0
    
