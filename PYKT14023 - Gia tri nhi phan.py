"""
    phần tử bắt đầu + 1
    phần tử kết thúc -1
    sử dụng mảng hiệu
"""
n, q = map(int, input().split())
diff = [0]*(n+2)

for _ in range(q):
    x, y = map(int, input().split())
    diff[x] += 1
    diff[y+1] -=1

for i in range(1,n+1):
    diff[i]+=diff[i-1]
for i in range(1,n+1):
    print(diff[i]%2,end=" ")
