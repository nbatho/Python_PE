f = [0]*95
def Init():
    f[1] = f[2] = 1
    for i in range(2,95):
        f[i] = f[i-1] + f[i-2]
Init()
for _ in range(int(input())):
    a, b = map(int,input().split())
    for i in range(a,b + 1):
        print(f[i],end = " ")
    print()
