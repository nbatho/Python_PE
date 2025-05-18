import math

def sieve(limit):
    prime = [True] * (limit + 1)
    prime[0] = prime[1] = False
    for i in range(2,int(math.sqrt(limit)) + 1):
        if prime[i]:
            for j in range(i*i,limit,i):
                prime[j] = False
    primes = []
    for i in range(2, limit + 1):
        if prime[i]:
            primes.append(i)
    return primes
n = int(input())
cnt = 0
primes = sieve(int(n ** 0.5) + 1)
for p in primes:
    if p**8 <= n:
        cnt += 1
    else:
        break
for i in range(len(primes)):
    p2 = primes[i] ** 2
    if p2 > n:
        break
    for j in range(i + 1, len(primes)):
        q2 = primes[j] ** 2
        if p2 * q2 <= n:
            cnt += 1
        else:
            break 


print(cnt)