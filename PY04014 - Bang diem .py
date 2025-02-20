from decimal import ROUND_HALF_UP, Decimal
cnt = 1
class HocSinh:
    diemTrungBinh = 0
    mhs = "HS"
    XepHang = ""
    def __init__(self,ten,diem):
        global cnt
        if cnt < 10:
            self.mhs += "0" + str(cnt)
        else:
            self.mhs += str(cnt)
        cnt += 1
        self.ten = ten
        x = 2*diem[0] + 2*diem[1]
        for i in range(2,10):
            x += diem[i]
        x/=12
        if x < 5 : self.XepHang = 'YEU'
        elif x < 7 : self.XepHang = 'TB'
        elif x < 8 : self.XepHang = 'KHA'
        elif x < 9 : self.XepHang = 'GIOI'
        else : self.XepHang = 'XUAT SAC'
        self.diemTrungBinh = x.quantize(Decimal('0.1'), ROUND_HALF_UP)
    def info(self):
        print(self.mhs,self.ten,self.diemTrungBinh,self.XepHang)


a = []
for _ in range(int(input())):
    ten = input()
    diem = [Decimal(x) for x in input().split()]
    a.append(HocSinh(ten,diem))
a = sorted(a,key = lambda x:( -x.diemTrungBinh,x.mhs))
for i in a:
    i.info()
