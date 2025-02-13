s = input().split()
max_len = 0
for i in s:
    if len(i) > max_len:
        max_len = len(i)
for i in s:
    if len(i) == max_len:
        print(i,max_len)