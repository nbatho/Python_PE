import math
def isPrime(n):
    if n < 2: return False
    for i in range(2,int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
def GCD( a,  b):
    while (b != 0):
        tmp = b
        b = a % b
        a = tmp
    return a
t = int(input())
while t != 0:
    n = int(input())
    k = 0

    for i in range(1, n):
        if GCD(n,i) == 1:
            k+=1
    if isPrime(k):
        print("YES")
    else: print("NO")
    t-=1

