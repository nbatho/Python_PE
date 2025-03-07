ao,bo,co = [int(x) for x in input().split()]
a1,b1,c1 = [int(x) for x in input().split()]

bdau = ao * 3600 + bo*60 + co
kthuc = a1 * 3600 + b1*60 + c1

if kthuc < bdau:
    kthuc += 24*3600
print(abs(kthuc - bdau))