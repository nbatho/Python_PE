n = int(input())
cnt = 0
a = []
while True:
    x = input().split()
    cnt += len(x)
    for i in x:
        a.append(int(i))
    if cnt == n:
        break
    
missing = []
for i in range(1,max(a) + 1):
    if i not in a:
        missing.append(i)

if len(missing) == 0:
    print("Excellent!")
else:
    for i in missing:
        print(i)
