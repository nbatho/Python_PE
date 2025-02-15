s = input()
k = int(input())
a = []
cnt = 0
tmp = ""
danhdau = [0]*100
for i in range(len(s)):
    tmp += s[i]
    cnt += 1
    if cnt % 2 == 0:
        a.append(int(tmp))
        cnt = 0
        tmp = ""
for i in a:
    danhdau[i]+=1
found = False
for i in range(100):
    if danhdau[i] >= k:
        found = True
        print(i,danhdau[i])
if found == False:
    print("NOT FOUND")