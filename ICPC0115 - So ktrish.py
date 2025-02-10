def fact(n):
    if n == 0 or n == 1: return 1
    prod = 1
    for i in range(1,n + 1):
        prod *=i
    return prod
for _ in range(int(input())):
    n = input()
    sum = 0
    for i in range(len(n)):
        sum += fact(int(n[i]))
    
    if sum == int(n): print("Yes")
    else:print("No")