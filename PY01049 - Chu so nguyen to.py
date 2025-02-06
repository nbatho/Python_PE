import math
def isPrime(n):
    for i in range(2,int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return n > 1
def Check(n):

    nt = 0
    knt = 0
    for i in range(0,len(n)):
        if (isPrime(int(n[i]))):nt+=1
        else:knt+=1
    return isPrime(len(n)) and nt > knt
for _ in range(int(input())):
    n = input()
    if (Check(n)): print("YES")
    else: print("NO")