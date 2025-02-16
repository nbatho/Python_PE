n ,m = map(int,input().split())

a = []
for i in range(n):
	x = list(map(int,input().split()))
	a.append(x)
min_value = 10001
max_value = -1
found = False
for i in range(n):
	for j in range(m):
		max_value = max(max_value,a[i][j])
		min_value = min(min_value,a[i][j])
for i in range(n):
	for j in range(m):
		if a[i][j] == abs(max_value - min_value):
			found = True
if found == False:
	print("NOT FOUND")
else:
	print(max_value - min_value)
	for i in range(n):
		for j in range(m):
			if a[i][j] == abs(max_value - min_value):
				print(f'Vi tri {[i]}{[j]}')
				found = True
