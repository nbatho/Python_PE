class TienDien:
    def __init__(self, id, ten, gd, dau, cuoi):
        if id < 10:
            self.ma = "KH0" + str(id)
        else:
            self.ma = "KH" + str(id)
        self.cuoi = int(cuoi)
        self.dau = int(dau)
        self.gd = gd
        self.ten = self.chuanhoa(ten)
        self.sodien = self.cuoi - self.dau
        self.trong = self.TienTrongDinhMuc(self.sodien, self.gd)
        self.vuot = self.TienVuotDinhMuc(self.sodien, self.gd)
        self.thueVAT = self.vuot // 20
        self.tong = self.trong + self.vuot + self.thueVAT

    def TienTrongDinhMuc(self, sodien, gd):
        if gd == "A": DinhMuc = 100
        elif gd == "B": DinhMuc = 500
        elif gd == "C": DinhMuc = 200

        if sodien < DinhMuc:
            return sodien * 450
        elif sodien >= DinhMuc:
            return DinhMuc*450

    def TienVuotDinhMuc(self, sodien, gd):
        if gd == "A": DinhMuc = 100
        elif gd == "B": DinhMuc = 500
        elif gd == "C": DinhMuc = 200

        if sodien > DinhMuc: return ((sodien - DinhMuc)*1000)
        else: return 0

    def chuanhoa(self, s):
        name = ""
        for i in s.split():
            name += i[0].upper() + i[1:] + " "
        return name.strip()

    def thongtin(self):
        print(f'{self.ma} {self.ten} {self.trong} {self.vuot} {self.thueVAT} {self.tong}')

ls = []
for i in range(int(input())):
    ten = input().lower()
    gd, dau, cuoi = input().split(" ")
    ls.append(TienDien(i+1, ten, gd, dau, cuoi))

ls = sorted(ls, key=lambda x: -x.tong)

for i in ls:
    i.thongtin()
