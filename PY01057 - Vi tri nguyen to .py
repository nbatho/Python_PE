import math
def isPrime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: return False
    return n > 1
def check(n) :
	for i in range(len(n)) :
		if isPrime(i) != isPrime(int(n[i])) : return 0
	return 1

for _ in range(int(input())):
    n = input()
    if check(n) == 1: print("YES")
    else: print("NO")