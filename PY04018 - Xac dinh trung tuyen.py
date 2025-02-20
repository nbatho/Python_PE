class Diem:
    def __init__(self,id,ten,ma,tin,cm):
        if id < 10: self.mgv = "GV0" + str(id)
        else: self.mgv = "GV" + str(id)
        self.ten = ten
        if ma[0] == "A": self.mon = "TOAN"
        elif ma[0] == "B": self.mon = "LY"
        elif ma[0] == "C": self.mon = "HOA"
        if ma[1] == "1": self.tongdiem = 2.0 + tin*2 + cm
        elif ma[1] == "2": self.tongdiem = 1.5 + tin*2 + cm
        elif ma[1] == "3": self.tongdiem = 1.0 + tin*2 + cm
        elif ma[1] == "4": self.tongdiem = 0.0 + tin*2 + cm
        if self.tongdiem < 18: self.TT = "LOAI"
        else: self.TT = "TRUNG TUYEN"
    def info(self): print(self.mgv,self.ten,self.mon,self.tongdiem,self.TT)
a = []
for i in range(int(input())):
    ten = input()
    ma = input()
    DiemTin = float(input())
    DiemChuyenMon = float(input())
    a.append(Diem(i+1,ten,ma,DiemTin,DiemChuyenMon))

a = sorted(a,key = lambda x: x.tongdiem,reverse=True)
for i in a:
    i.info()