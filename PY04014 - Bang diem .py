class Diem:
    def __init__(self,id,ten,diem):
        if id < 10:
            self.ma = "HS0" + str(id)
        elif id < 100:
            self.ma = "HS" + str(id)
        self.ten = ten
        self.tb = diem[0]*2 + diem[1]*2
        for i in range(2,10):
            self.tb += diem[i]
        
        self.tb /= 12
        self.xep_hang = ""
        if self.tb < 5 : self.xep_hang = 'YEU'
        elif self.tb < 7 : self.xep_hang = 'TB'
        elif self.tb < 8 : self.xep_hang = 'KHA'
        elif self.tb < 9 : self.xep_hang = 'GIOI'
        else : self.xep_hang = 'XUAT SAC'
        self.tb = round(self.tb + 1e-8, 1)
    def output(self):
        print(self.ma,self.ten,self.tb,self.xep_hang)
a = []
for i in range(int(input())):
    ten = input()
    diem_mon = [float(x) for x in input().split()]
    a.append(Diem(i+1,ten,diem_mon))
a = sorted(a,key= lambda x: (-x.tb,x.ma) )
for i in a:
    i.output()
    