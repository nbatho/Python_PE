class HoaDon:
    def __init__(self,ma,ten,sl,gia,chietkhau):
        self.ma = ma
        self.ten = ten
        self.sl = sl
        self.gia =gia
        self.chietkhau = chietkhau
        self.tong = (self.gia * self.sl) - self.chietkhau
    def info(self):
        print(self.ma,self.ten,self.sl,self.gia,self.chietkhau,self.tong)
a = []
for _ in range((int(input()))):
    ma = input()
    ten = input()
    sl = int(input())
    gia = int(input())
    chietkhau = int(input())
    a.append(HoaDon(ma,ten,sl,gia,chietkhau))
a = sorted(a,key = lambda x:-x.tong)
for i in a:
    i.info()
