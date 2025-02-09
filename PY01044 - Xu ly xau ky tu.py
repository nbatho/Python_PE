s1 = input().lower().split()
s2 = input().lower().split()
Hop = []
Giao = []
TrungGian =[]
for i in s1:
    if i not in Hop:
        Hop.append(i)
        TrungGian.append(i)
for i in s2:
    if i not in Hop:
        Hop.append(i)
    if i in TrungGian and i not in Giao:
        Giao.append(i)
Hop = sorted(Hop)
Giao = sorted(Giao)
for i in Hop:
    print(i,end = " ")
print()
for i in Giao:
    print(i,end = " ")