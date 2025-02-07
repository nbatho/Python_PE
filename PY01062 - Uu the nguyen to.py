import math
def isPrime(n):
    for i in range(2 , int(math.sqrt(n)) + 1):
        if n % i == 0: return False
    return n >1

for _ in range(int(input())):
    n = input()

    prime = 0 
    nonprime = 0
    for i in range(0,len(n)):
        if isPrime(int(n[i])): prime +=1
        else: nonprime +=1

    if isPrime(len(n)) and prime > nonprime: print("YES")
    else: print("NO")