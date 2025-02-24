import functools
class SinhVien:
    def __init__(self,ten,dung,submit):
        self.ten = ten
        self.dung = dung
        self.submit = submit

    def info(self):
        print(self.ten,self.dung,self.submit)
def cmp(a,b):
    if a.dung < b.dung: return 1
    elif a.dung == b.dung:
        if a.submit > b.submit: return 1
        elif a.submit == b.submit:
            if a.ten > b.ten: return 1
            else: return -1
        else: return -1
    else: return -1
a = []        
for _ in range(int(input())):
    s = input()
    c,t = [int(x) for x in input().split()]
    a.append(SinhVien(s,c,t))
a = sorted(a, key = functools.cmp_to_key(cmp))
for i in a:
    i.info()