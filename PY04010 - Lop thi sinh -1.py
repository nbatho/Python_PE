class ThiSinh:
    sum = 0
    def __init__(self,ten,ns,dm1,dm2,dm3):
        self.ten = ten
        self.ns = ns
        self.dm1 = dm1
        self.dm2 = dm2
        self.dm3 = dm3
        self.sum = self.dm1 + self.dm2 + self.dm3
    def inketqua(self): 
        print(self.ten,self.ns,"{:.1f}".format(self.sum))

hoten = input()
ns = input()
diem1 = float(input())
diem2 = float(input())
diem3 = float(input())

data = ThiSinh(hoten,ns,diem1,diem2,diem3)
data.inketqua()