cnt = 1 
class HoaDon:
    maKH = "KH"
    tong = 0
    def __init__(self,ten,csc,csm):
        global cnt
        if cnt < 10:
            self.maKH += "0" + str(cnt)
        else:
            self.maKH += str(cnt)
        cnt += 1
        self.ten = ten
        self.csc = csc
        self.csm = csm
        chenhlech = self.csm - self.csc

        if chenhlech >= 0 and chenhlech <= 50:
            self.tong = chenhlech*100*(1.02)
        elif chenhlech >= 51 and chenhlech <= 100:
            self.tong = (50*100 + (chenhlech - 50)*150)*1.03
        elif chenhlech > 100:
            self.tong = (50*100 + 50*150 + (chenhlech - 100)*200)*1.05
        self.tong = round(self.tong)
    def info(self):
        print(self.maKH,self.ten,self.tong)
a = []
for _ in range(int(input())):
    ten = input()
    csc = int(input())
    csm = int(input())
    a.append(HoaDon(ten,csc,csm))
a = sorted(a,key = lambda x: x.tong,reverse= True)
for i in a:
    i.info()