m = int(input())
v = int(input())
t = int(input())
d = input()
if d == 'C':
    print((v*t)%m)
elif d =='A':
    print(((m-(v*t))%m)%m)