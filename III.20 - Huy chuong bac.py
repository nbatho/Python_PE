n = int(input())
ls = []
for i in range(n):
    x = int(input())
    ls.append(x)
ls.sort()
print(f'Silver = {ls[-2]}')