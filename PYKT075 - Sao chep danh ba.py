file = open("E:/Python_PE/SOTAY.txt")
out = open("E:/Python_PE/DIENTHOAI.txt", "w")
ls = []
for data in file:
    ls.append(data.strip())
ans = []
q = []
Split = []
for i in range(len(ls)):
    if "Ngay" in ls[i]:
        x = ls[i].split()
        q.append(i)
        Split.append(x[1])

i = 0
cnt = 0
while i != len(ls):
    if i in q:
        cnt +=1
        i +=1
    tmp = ls[i] + ": " + ls[i+1]
    ans.append({tmp:cnt-1})
    i+=2
    
for item in ans:
    for k, v in item.items():
        out.write(f"{k} {Split[v]}\n")

file.close()
out.close()
