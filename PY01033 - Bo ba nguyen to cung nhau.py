import math
def check(a,b,c): return math.gcd(a,b) == 1 and math.gcd(b,c) == 1 and math.gcd(a,c) == 1 and a < b and b < c

l , r = map(int,input().split())

for i in range(l,r + 1):
    for j in range(i+1,r + 1):
        for k in range(j+1,r + 1):
            if (check(i,j,k)):
                print("(",sep = "",end = "")
                print(i,j,k, sep =", ",end = "")
                print(")",sep = "",end = "\n")