import math
def prime(n):
    for i in range(2,int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return n > 1
n = int(input())
a = list(map(int,input().split()))
b = []

for i in a:
    if i not in b:
        b.append(i)
prefix = [0]*len(b)
prefix[0] = b[0]
found = False
for i in range(1,len(b)):
    prefix[i] += prefix[i-1] + b[i]
for i in range(len(prefix)):
    if prime(prefix[i]) and prime(prefix[len(prefix) - 1] - prefix[i]):
        print(i)
        found = True
        break

if found == False:
    print("NOT FOUND")
