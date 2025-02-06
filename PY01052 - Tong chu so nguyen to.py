import math
def isPrime(n):
    for i in range(2,int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return n > 1

for _ in range(int(input())):
    n = input()
    digit_sum = 0
    for i in range(0,len(n)):
        digit_sum += int(n[i])

    if isPrime(digit_sum): print("YES")
    else: print("NO")