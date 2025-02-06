import math
def isPrime(n):
    for i in range(2,int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return n > 1

for _ in range(int(input())):
    n = input()
    ans = ""
    for i in range(len(n) - 4, len(n)):
        ans += n[i]
    if (isPrime(int(ans))) :print("YES")
    else:print("NO")