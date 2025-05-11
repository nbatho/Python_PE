from datetime import datetime
class Lich:
    def __init__(self,ngay,gio,id,ten_mon,nhom,ssv,ma_ca_thi):
        self.ngay = ngay
        self.gio = gio
        self.id = id
        self.ten_mon = ten_mon
        self.nhom = nhom 
        self.ssv =ssv
        self.ma_ca_thi = ma_ca_thi
        self.thoigian = datetime.strptime(ngay + " " + gio, "%d/%m/%Y %H:%M")
    def output(self):
        print(self.ngay,self.gio,self.id,self.ten_mon,self.nhom,self.ssv)
f1 = open("MONTHI.in")
f2 = open("CATHI.in")
f3 = open("LICHTHI.in")
so_mon_hoc = f1.readline()
mon = []
for _ in range(int(so_mon_hoc)):
    ma_mon = f1.readline().strip()
    ten_mon = f1.readline().strip()
    hinh_thuc_thi = f1.readline().strip()
    mon.append((ma_mon,(ten_mon,hinh_thuc_thi)))

ca_thi = f2.readline()
ca = []
for _ in range(int(ca_thi)):
    ngay = f2.readline().strip()
    gio = f2.readline().strip()
    id = f2.readline().strip()
    ca.append(((ngay,gio),id))
so_luong_dong = f3.readline()
# print(ca[0])
ans = []
for _ in range(int(so_luong_dong)):
    ma_ca_thi,ma_mon,ma_nhom,ssv = f3.readline().split()
    tt = int(ma_ca_thi[1:])
    
    for i in range(len(ca)):
        if i == tt - 1:
            Ngay = ca[i][0][0]
            Gio = ca[i][0][1]
            Id = ca[i][1]
    
    for ten in mon:
        if ten[0] == ma_mon:
            Ten_mon = ten[1][0]
    ans.append(Lich(Ngay,Gio,Id,Ten_mon,ma_nhom,ssv,ma_ca_thi))
ans = sorted(ans, key= lambda x: (x.thoigian,x.ma_ca_thi))
for i in ans:
    i.output()
f1.close()
f2.close()
f3.close()
