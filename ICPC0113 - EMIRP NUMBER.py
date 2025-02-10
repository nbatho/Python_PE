import math
def isPrime(n):
    for i in range(2,int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return n > 1

def Dao(num):
    reverse = 0
    while num != 0:
        reverse = reverse*10 + num %10
        num //=10
    return reverse
for _ in range(int(input())):
    n = input()
    for i in range(13,int(n)):
        dao = Dao(i)
        if isPrime(i) and isPrime(dao) and i != dao and i < dao:
            if i < int(n) and dao < int(n):
                print(i,dao,end = " ")
    print()