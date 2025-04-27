import datetime as dt
class KS:
    def __init__(self,id,ten,phong,so_ngay,dv):
        if id < 10:
            self.ma = "KH0" + str(id)
        else:
            self.ma = "KH" + str(id) 
        self.ten = ten
        self.phong = phong
        self.gia = None
        if self.phong[0] == '1':
            self.gia = 25
        elif self.phong[0] == '2':
            self.gia = 34
        elif self.phong[0] == '3':
            self.gia = 50
        elif self.phong[0] == '4':
            self.gia = 80
        self.so_ngay = so_ngay
        self.dv =dv
        self.tong = self.gia * self.so_ngay + self.dv
    def output(self):
        print(self.ma,self.ten,self.phong,self.so_ngay,self.tong)
a = []
for i in range(int(input())):
    tenKH = input().strip()
    phong = input().strip()
    nhan = input().strip().split('/')
    tra = input().strip().split('/')
    dv = int(input())
    c_in = dt.date(int(nhan[2]),int(nhan[1]),int(nhan[0]))
    c_out = dt.date(int(tra[2]),int(tra[1]),int(tra[0]))
    so_ngay = c_out - c_in
    a.append(KS(i+1,tenKH,phong,so_ngay.days+1,dv))

a = sorted(a,key= lambda x:-x.tong)
for i in a:
    i.output()