def checkTN(n):
    if len(n) < 2: return False

    for i in range(len(n) // 2):
        if n[i] != n[len(n) - 1 - i]:
            return False
        
    return True
n , m = map(int,input().split())

a = []
for i in range(n):
    x = list(map(int,input().split()))
    a.append(x)
max_value = -1
for i in range(n):
    for j in range(m):
        if checkTN(str(a[i][j])):
            max_value = max(max_value,a[i][j])

if max_value == -1:
    print("NOT FOUND")
else:
    print(max_value)
    for i in range(n):
        for j in range(m):
            if max_value == a[i][j]:
                print(f'Vi tri {[i]}{[j]}')