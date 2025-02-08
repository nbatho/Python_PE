#  luu vi tri cua cac benh nhan truoc
#  tinh tong so nguoi co nguy co xung quanh cac benh 

m , n = map(int,input().split())
direct = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

matrix = []

for i in range(m):
    row =list(map(int, input().split()))
    matrix.append(row)
ans = 0
q = []
for i in range(m):
    for j in range(n):
        if (matrix[i][j] == -1):
            q.append([i,j])
            
while len(q) > 0:
    u = q[0]
    q.pop(0)
    for first, second in direct:
        inew = u[0] + first
        jnew = u[1] + second
        if (inew >= 0 and inew < m and jnew >= 0 and jnew < n):
            if matrix[inew][jnew] != 0:
                ans += matrix[inew][jnew]
                matrix[inew][jnew] = 0
print(ans)