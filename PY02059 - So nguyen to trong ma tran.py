import math
def prime(n):
	for i in range(2,int(math.sqrt(n)) + 1):
		if n % i == 0: return False

	return n >1
n ,m = map(int,input().split())

a = []
for i in range(n):
	x = list(map(int,input().split()))
	a.append(x)
max_value = -1
found = False
for i in range(n):
	for j in range(m):
		if (prime(a[i][j])):
			max_value = max(max_value,a[i][j])
if max_value == -1:
	print("NOT FOUND")
else:
	print(max_value)
	for i in range(n):
		for j in range(m):
			if a[i][j] == abs(max_value):
				print(f'Vi tri {[i]}{[j]}')
