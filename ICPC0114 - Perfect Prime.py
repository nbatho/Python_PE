import math
def prime(n):
    for i in range(2 , int(math.sqrt(n)) + 1):
        if n % i == 0: return False
    return n > 1

def check(n):
    dao = n[::-1]
    sum = 0
    for i in range(0,len(n)):
        if prime(int(n[i])) == False: return False
        sum += int(n[i])
    return prime(int(n)) and prime(sum) and prime(int(dao))
for _ in range(int(input())):
    n = input()
    if check(n): print("Yes")
    else: print("No")