class SinhVien:
    def __init__(self,msv,ten,lop,vang):
        self.msv = msv
        self.ten = ten
        self.lop = lop
        self.diem = 10
        for i in range(len(vang)):
            if vang[i] == "v": self.diem -=2
            elif vang[i] == "m": self.diem -=1
        if self.diem < 0:
            self.diem = 0
    def info(self):
        print(self.msv,self.ten,self.lop,self.diem,sep = " ",end = "")
        if self.diem == 0:
            print(" KDDK")
        else: print()

n = int(input())
a = {}

for _ in range(n):
    ls = []
    msv = input()
    ten = input()
    lop = input()
    a[msv] = [ten,lop, ""]
for i in range(n):
    msv, vang = input().strip().split()
    if msv in a:
        a[msv][2] += vang
danhsach = [SinhVien(msv, ten, lop, vang) for msv, (ten, lop, vang) in a.items()]

for i in danhsach:
    i.info()