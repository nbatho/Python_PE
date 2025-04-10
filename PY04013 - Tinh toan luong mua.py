#PY04013 - Tinh toan luong mua
class Rain:
    def __init__(self,id,ten,tg,luongmua):
        if id < 10:
            self.ma = "T0" + str(id)
        else: self.ma = "T" + str(id)
        self.gio = tg / 60
        self.tb_luong_mua = luongmua / self.gio
        self.ten = ten
    def thong_tin(self):
        print(self.ma,self.ten,f'{self.tb_luong_mua:.2f}')     
        

def convertTime(t):
    s = t.split(":")
    hh = int(s[0])
    mm = int(s[1])
    return hh*60 + mm
ls = {}
for _ in range(int(input())):
    ten = input()
    start = input()
    end = input()
    luongmua = int(input())
    if ten not in ls:
        ls[ten] = {
            "tg": convertTime(end) - convertTime(start),
            "luongmua":luongmua
        }
    else:     
        ls[ten]["tg"] += convertTime(end) - convertTime(start)
        ls[ten]["luongmua"] += luongmua
a = []
for i , (key,value) in enumerate(ls.items()):
    a.append(Rain(i+1,key,value["tg"],value["luongmua"]))

for i in a:
    i.thong_tin()