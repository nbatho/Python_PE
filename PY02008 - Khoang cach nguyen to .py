import math
limit =10001

def sieve(limit):
    prime=[True]*limit
    prime[0] = prime[1] =False
    for i in range(2,int(math.sqrt(limit)) +1):
        if prime[i]:
            for j in range(i*i,limit,i):
                prime[j] = False
    primes =[]
    for i in range(2,limit):
        if prime[i]:
            primes.append(i)
    return primes
                
     
n ,k= map(int,input().split())
primes=sieve(limit)
cnt =0
print(k,end=" ")
for i in range(n):
    k+=primes[i]
    print(k,end=" ")