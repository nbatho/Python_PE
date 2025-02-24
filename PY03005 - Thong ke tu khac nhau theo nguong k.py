n, k = [int (x)  for x in input().split()]
mp = {} 
for _ in range(n):
    s = input().lower()
    tmp = ""

    for char in s:
        if (char >= 'a' and char <= 'z') or(char >= '0' and char <= '9'):
            tmp += char
        else:
            if tmp != '':
                if tmp in mp: 
                    mp[tmp] += 1
                else:
                    mp[tmp] = 1
                tmp = ""
        
    if tmp != '':
        if tmp in mp: 
            mp[tmp] += 1
        else:
            mp[tmp] = 1

m = sorted(mp.items(), key=lambda x: (-x[1], x[0]))
for i in m:
    if i[1] >= k:
        print(i[0],i[1])