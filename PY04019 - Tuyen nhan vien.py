
class NhanVien:
    def __init__(self,maTS, ten, lt, th):
        self.maTS = 'TS0' + str(maTS)
        self.ten = ten
        self.lt = lt
        self.th = th

        if self.lt > 10: self.lt /= 10
        if self.th > 10: self.th /= 10
        
        self.diem_TB = (self.lt + self.th) / 2

        if self.diem_TB < 5.0:
            self.TrangThai = "TRUOT"
        elif self.diem_TB < 8.0:
            self.TrangThai = "CAN NHAC"
        elif self.diem_TB < 9.5:
            self.TrangThai = "DAT"
        else:
            self.TrangThai = "XUAT SAC"

    def info(self):
        print(self.maTS, self.ten, '{:.2f}'.format(self.diem_TB), self.TrangThai)

a = []
for i in range(int(input())):
    ten = input().strip()
    lythuyet = float(input())
    thuchanh = float(input())
    a.append(NhanVien(i+1,ten,lythuyet, thuchanh))

a.sort(key=lambda x: x.diem_TB,reverse= True)

for i in a:
    i.info()
