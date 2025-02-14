import math
def ToHop(n,k):
    if n < k :return 0
    return math.factorial(n) // (math.factorial(k) * math.factorial(n-k))
n = int(input())
matrix = []
for i in range(n):
    tmp = input().split()
    for char in tmp:
        matrix.append(char)
ans = 0
for i in range(n):
    cnt = 0
    for j in range(n):
        if matrix[i][j] == 'C': cnt += 1
    ans += ToHop(cnt,2)
for i in range(n):
    cnt1 = 0
    for j in range(n):
        if matrix[j][i] == 'C':cnt1 += 1
    ans += ToHop(cnt1,2)
print(ans)