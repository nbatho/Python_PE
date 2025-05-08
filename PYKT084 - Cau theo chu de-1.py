ans = []
a = []
for _ in range(int(input())):
    s = input()
    a.append(s.strip())  

cnt = 0
first = True
key = None

for i in range(len(a)):
    if first:
        key = a[i]
        ans.append({key: 0})
        first = False
    elif a[i] == '':
        cnt = 0
        first = True
        key = None
    else:
        cnt += 1
        ans[-1][key] = cnt 
for item in ans:
    for k, v in item.items():
        print(f"{k}: {v}")
