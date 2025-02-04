import math
def GCD(a,b):
    while (b != 0):
        tmp = b
        b = a % b
        a = tmp
    return a
def isPrime(n):
    for i in range(2 , int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return n> 1

def Sum(n):
    sum = 0
    while (n != 0):
        sum += n%10 
        n//=10
    return sum
tc = int(input())
for i in range(0,tc):
    a , b = map((int),input().split())
    if (isPrime(Sum(GCD(a,b)))): print("YES")
    else: print("NO")
    