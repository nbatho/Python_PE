import math
def isPrime(n):
    for i in range(2,int(math.sqrt(n))):
        if n % i == 0: return False
    return n > 1
def check(n):
    digit_sum = 0
    ok = True
    for i in range(0,len(n)):
        digit_sum += int(n[i])
        if  (i % 2 == 0 and int(n[i]) % 2 != 0) or (i% 2 != 0 and int(n[i]) % 2 == 0):
           ok = False

    return isPrime(digit_sum) and ok == True

for _ in range(int(input())):
    n = input()

    if (check(n)): print("YES")
    else: print("NO")