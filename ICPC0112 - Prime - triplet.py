import math
MAX = 1000005
prime = [True]*MAX
def Seive():
    prime[0] = prime[1] = False
    for i in range(2,int(math.sqrt(MAX)) + 1):
        if prime[i]:
            for j in range(i*i,MAX,i):
                prime[j] = False


Seive()

for _ in range(int(input())):
    ans = 0
    n = int(input())
    for i in range(n - 5):
        if prime[i] and prime[i+6]:
            if prime[i+2] or prime[i+4]:
                ans += 1
    print(ans)
        
        