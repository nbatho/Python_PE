class Lich:
    def __init__(self,ma,ma_mon,ten_mon,date,time,group):
        if ma < 10:
            self.ma_ca_thi = "T00" + str(ma)
        elif ma < 100:
            self.ma_ca_thi = "T0" + str(ma)
        else: self.ma_ca_thi = "T" + str(ma)

        self.ma = ma
        self.ma_mon = ma_mon
        self.ten_mon = ten_mon
        self.date = date
        self.ngay = int(date[:2:])
        self.thang = int(date[3:5:])
        self.nam = int(date[6::])
        self.time = time
        self.gio = int(time[:2:])
        self.phut = int(time[3::])
        self.group = group
    
    def xuat(self):
        print(self.ma_ca_thi,self.ma_mon,self.ten_mon,self.date,self.time,self.group)

n , m = [int(x) for x in input().split()]
ls_mon_hoc = []
ls = []
for i in range(n):
    tmp = []
    for i in range(2):
        tmp.append(input())

    ls_mon_hoc.append(tmp)
for i in range(m):
    s = input().split()
    ma_mon = s[0]
    date = s[1]
    time = s[2]
    group = s[3]
    for j in ls_mon_hoc:
        if ma_mon == j[0]:
            ten_mon = j[1]
    ls.append(Lich(i+1,ma_mon,ten_mon,date,time,group))

ls = sorted(ls, key = lambda x : (x.nam, x.thang, x.ngay, x.gio, x.phut, x.ma_mon))
for i in ls:
    i.xuat()