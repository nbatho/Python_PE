import math
def prime(n):
    for i in range(2,int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return n > 1

n = int(input())
a = list(map(int, input().split()))
prime_value = []
idx = [0]*n
non_prime = []
for i in range(n):
    if prime(a[i]):
        prime_value.append(a[i])
        idx[i] = 1
    else: non_prime.append(a[i])
prime_value.sort()
k = 0
h = 0
for i in range(n):
    if idx[i] == 1:
        print(prime_value[k],end = " ")
        k +=1
    else:
        print(non_prime[h],end = " ")
        h+=1

