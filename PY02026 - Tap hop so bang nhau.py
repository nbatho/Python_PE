n,m =map(int,input().split())
a = list(map(int,input().split())) 
b = list(map(int,input().split()))

set_a = set(a)
set_b = set(b)

if set_a == set_b:
    print("YES")
else:
    print("NO")