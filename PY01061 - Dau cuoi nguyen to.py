import math
def isPrime(n):
    for i in range(2 , int(math.sqrt(n)) + 1):
        if n % i == 0: return False
    return n >1
for _ in range(int(input())):
    n = input()
    size = len(n)
    dau = n[0] + n[1] + n[2]
    cuoi = n[size - 3] + n[size - 2] + n[size - 1]
    if isPrime(int(dau)) and isPrime(int(cuoi)): print("YES")
    else:print("NO")
