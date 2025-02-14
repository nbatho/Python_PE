import math
def prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: return False
    return n > 1
n , m = map(int,input().split())
a = []
for i in range(n):
    x = list(map(int,input().split()))
    a.append(x)

for i in range(n):
    for j in range(m):
        if prime(a[i][j]):
            print(1, end = " ")
        else: print(0,end = " ")
    print()