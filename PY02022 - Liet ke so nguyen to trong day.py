import math
def prime(n):
    for i in range(2,int(math.sqrt(n)) + 1):
        if n % i == 0: return False
    return n > 1

n = int(input())
a = list(map(int,input().split()))
freq = {}
pos = []
for num in a:
    if prime(num):
        if num not in freq:
            freq[num] = 0
            pos.append(num)
        freq[num] += 1
for num in pos:
    print(num,freq[num])