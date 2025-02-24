class BXH:
    def __init__(self, ten, dv, time):
        self.ten = ten
        self.dv = dv
        self.time = time
        self.vt = self.velocity() 
        self.ma = self.generate_id()  
    
    def velocity(self):
        s = self.time.split(':')
        tg = 120 / (int(s[0]) - 6 + int(s[1]) /60)
        return tg
    
    def generate_id(self):
        ma = ""
        for i in self.dv.split():
            ma += i[0]
        for i in self.ten.split():
            ma += i[0]
        return ma
    
    def info(self):
        return f"{self.ma} {self.ten} {self.dv} {round(self.vt)} Km/h"

a = []
for _ in range(int(input())):
    ten = input()
    dv = input()
    time = input()
    a.append(BXH(ten, dv, time))

a.sort(key=lambda x: -x.vt)
for i in a:
    print(i.info())
